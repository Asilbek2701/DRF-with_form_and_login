from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thankyou")
    else:
        form = UserRegisterForm()

    context = {"form": form}
    return render(request, "register.html", context)


def thankyou(request):
    return render(request, 'thankyou.html')

class UserList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
