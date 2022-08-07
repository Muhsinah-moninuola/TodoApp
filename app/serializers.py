from app.models import *
from rest_framework import serializers
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','item', 'created_at']


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=30, min_length=4)
    class Meta:
        model = User
        fields =['id', 'email', 'password', 'first_name', 'last_name', 'username', 'phone_number']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')}
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('Username is already in use')}
            )
        return super().validate(attrs)