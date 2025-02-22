from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='')

class TransferSessionForm(forms.Form):
    session_id = forms.CharField(max_length=100, label='Identyfikator sesji')
    