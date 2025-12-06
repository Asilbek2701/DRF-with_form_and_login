from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm
from rest_framework.generics import ListAPIView

from .serializers import User, UserSerializer



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                subject='Welcome to DFR',
                from_email=settings.EMAIL_HOST_USER,
                message=f'Welcome {user.username}! You have successfully registered!',
                recipient_list=[user.email],
                fail_silently=False,
            )
            return redirect(thankyou)
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'emails/register.html', context)

def thankyou(request):
    return render(request, 'emails/thankyou.html')


class EmailListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer