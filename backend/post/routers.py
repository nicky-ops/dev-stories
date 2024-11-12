from .viewsets import PostViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
]