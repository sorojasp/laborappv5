from rest_framework import serializers
from task import models
# from django.contrib.auth.models import User
from user import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ['id', 'password', 'last_login', 'email','date_of_birth', 'is_active', 'is_admin']


