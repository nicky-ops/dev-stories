from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth.abstract.serializers import AbstractSerializer
from auth.serializers import UserSerializer
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
    
    def to_representation(self, instance):
        '''
        Return the user representation in the post serializer
        '''
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data

        return rep
    
    def update(self, instance, validated_data):
        '''
        Update the post
        '''
        if not instance.edited:
            validated_data['edited'] = True

        instance = super().update(instance, validated_data)
        return instance
    
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_liked(self, instance):
        '''
        Get the liked field
        '''
        request = self.context.get('request', None)

        if request is None or request.user.is_anonymous:
            return False
        
        return request.user.has_liked(instance)
    
    def get_likes_count(self, instance):
        '''
        Get the likes count
        '''
        return instance.liked_by.count()
    
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated', 'image']
        read_only_fields = ['edited']