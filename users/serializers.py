from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    queryset = CustomUser.objects.all()
    class Meta:
        model = CustomUser
        fields = '__all__'