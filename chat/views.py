import uuid
import openai
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Session, Message, Report, Prompt, Context
from .forms import ChatForm, TransferSessionForm
from django.conf import settings
from django.core.mail import send_mail

def get_session(request):
    session_id = request.COOKIES.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        session = Session.objects.create(session_id=session_id)
        response = redirect('chat')
        response.set_cookie('session_id', session_id, max_age=1209600)  # 2 tygodnie
        return response
    else:
        session, created = Session.objects.get_or_create(session_id=session_id)
        return session

def chat_view(request):
    if 'session_id' not in request.COOKIES:
        return get_session(request)
    session_id = request.COOKIES.get('session_id')
    session = Session.objects.get(session_id=session_id)
    messages = Message.objects.filter(session=session).order_by('timestamp')
    form = ChatForm()
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            Message.objects.create(session=session, sender='user', content=user_message)
            # Generowanie odpowiedzi z OpenAI
            openai.api_key = settings.OPENAI_API_KEY
            conversation = [{'role': msg.sender, 'content': msg.content} for msg in messages]
            conversation.append({'role': 'user', 'content': user_message})
            # Dodajemy prompt (jeśli istnieje)
            prompt = Prompt.objects.first()
            if prompt:
                conversation.insert(0, {'role': 'system', 'content': prompt.content})
            # Dodajemy kontekst (opcjonalnie)
            # Zakładamy, że Context jest już wektoryzowany i można go użyć
            # To wymaga dodatkowej implementacji
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
            bot_reply = response['choices'][0]['message']['content']
            Message.objects.create(session=session, sender='bot', content=bot_reply)
            return redirect('chat')
    context = {
        'session_id': session.session_id,
        'messages': messages,
        'form': form,
    }
    return render(request, 'chat/chat.html', context)

def report_view(request):
    session_id = request.COOKIES.get('session_id')
    if not session_id:
        return redirect('chat')
    session = Session.objects.get(session_id=session_id)
    Report.objects.create(session=session)
    # Wysłanie e-maila do administratora
    admin_email = settings.EMAIL_HOST_USER
    send_mail(
        subject='Nowe zgłoszenie - Chatbot',
        message=f'Zgłoszono sesję: {session.session_id}\nLink: {request.build_absolute_uri()}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[admin_email],
    )
    return HttpResponse('Zgłoszenie zostało wysłane.')

def transfer_session_view(request):
    form = TransferSessionForm()
    if request.method == 'POST':
        form = TransferSessionForm(request.POST)
        if form.is_valid():
            session_id = form.cleaned_data['session_id']
            response = redirect('chat')
            response.set_cookie('session_id', session_id, max_age=1209600)
            return response
    context = {
        'form': form,
    }
    return render(request, 'chat/transfer_session.html', context)

