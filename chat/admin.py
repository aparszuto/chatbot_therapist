from django.contrib import admin
from .models import Session, Message, Report, Prompt, Context

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['session', 'sender', 'timestamp']
    list_filter = ['sender', 'timestamp']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['session', 'reported_at']

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Context)
class ContextAdmin(admin.ModelAdmin):
    list_display = ['title']
