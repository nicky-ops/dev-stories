from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status

from auth.abstract.viewsets import AbstractViewSet
from .models import Post
from .serializers import PostSerializer


class UserPermission(BasePermission):
    '''
    Custom permission class to check permission of users:  all users can read the posts without authentication while only author and admin have permission to write 
    '''
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        
        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            
            return bool(request.user and request.user.is_authenticated)
        
        return False


class PostViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        '''
        Return all the posts
        '''
        return Post.objects.all()
    
    def get_object(self):
        '''
        Get a single post using public_id
        '''
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj
    
    def create(self, request, *args, **kwargs):
        '''
        Create a new post
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
