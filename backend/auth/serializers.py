from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from .abstract.serializers import AbstractSerializer
from .models import User

class UserSerializer(AbstractSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active', 'created', 'updated']
        read_only_fields = ['is_active']


class RegisterSerializer(UserSerializer):
    '''
    Registration serializer for requests and user creation
    '''
    # Making sure the password is at least 8 characters long, and no more than 128 and can't be read by the user
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        '''Using the create_user method to create a newuser'''
        return User.objects.create_user(**validated_data)
    

class LoginSerializer(TokenObtainPairSerializer):
    '''
    Login serializer for requests
    '''
    def validate(self, attrs):
        data = super().validate(attrs)
    
        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data