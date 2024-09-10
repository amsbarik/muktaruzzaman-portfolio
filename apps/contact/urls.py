from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contact, name='contact'),
    
    # admin contact message
    path('messages/', views.client_messages, name='messages'),
    path('message/update/<int:contact_id>/', views.message_status_update, name='message_status_update'),
]
