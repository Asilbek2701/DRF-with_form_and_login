from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, thankyou, EmailListView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='emails/login.html'), name='login'),
    path('thankyou/', thankyou, name='thankyou'),
    path('list/', EmailListView.as_view(), name='list'),
]