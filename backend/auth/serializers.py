from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email', 'is_active', 'created', 'updated']
        read_only_fields = ['is_active']

