from django.urls import path
from .views import account, home
urlpatterns = [
    path('', home.index, name='index'),
    path('register/', account.register, name='register'),
    path('send/sms', account.send_sms, name='send_sms'),
    path('login/sms/', account.login_sms, name='login_sms'),
    path('login/', account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('image/code/', account.image_code, name='image_code'),
]