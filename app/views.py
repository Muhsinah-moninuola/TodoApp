from django.shortcuts import render
from app.serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class TodogetApi(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

class Todoupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

class UserRegistrationAPIView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

   
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.create(validated_data = request.data)
            user.password = make_password(user.password)
            user.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


# Create your views here.
