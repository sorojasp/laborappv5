from django.shortcuts import render
#from django.contrib.auth.models import User
from user.models import MyUser as User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from user import serializer
# Create your views here.


class UserView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


    def list(self, request, *args, **kwargs):
        serializer_obj = self.serializer_class(self.queryset, many=True)
        print(serializer_obj.data)
        return Response({"dia": serializer_obj.data})

