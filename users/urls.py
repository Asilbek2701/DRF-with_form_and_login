from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register, thankyou, UserList


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('thankyou/', thankyou, name='thankyou'),
    path('list/', UserList.as_view(), name='list'),
]