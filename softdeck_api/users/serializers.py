from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField

'''
user_id,     -> IntegerField 
first_name,   -> Charfield 
last_name,    -> Charfield
email,        -> EmailField
password      -> Charfield
'''
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
'''
class LoginSerializer(serializers.ModelSerializer):

    password = PasswordField()

    class Meta:
        model = User
        field = ('username', 'email', 'first_name', 'last_name', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ['token']

        def validate_password(self, password):
            if validate_password(password) is None:
                return make_password(password)'''