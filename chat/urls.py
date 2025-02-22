from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('report/', views.report_view, name='report'),
    path('transfer/', views.transfer_session_view, name='transfer_session'),
]
