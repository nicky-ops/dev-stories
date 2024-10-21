from rest_framework import routers
from .viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
]