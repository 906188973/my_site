from django.urls import path
from .views import account
urlpatterns = [
    path('', account.index, name='index'),
    path('register/', account.register, name='register'),
    path('send/sms', account.send_sms, name='send_sms'),
]