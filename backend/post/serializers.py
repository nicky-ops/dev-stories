from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth.abstract.serializers import AbstractSerializer
from .models import Post
from auth.models import User


class PostSerializer(AbstractSerializer):
    '''
    Post serializer
    '''
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        '''
        Validate author field
        '''
        if self.context['request'].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated', 'image']
        read_only_fields = ['edited']