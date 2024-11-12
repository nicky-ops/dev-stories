from django.db import models
from auth.abstract.models import AbstractModel, AbstractManager
from devstories.settings import AUTH_USER_MODEL


class PostManager(AbstractManager):
    '''
    Custom post manager
    '''
    pass


class Post(AbstractModel):
    """
    Post model
    """
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    objects = PostManager()
    def __str__(self):
        return f"{self.author.name}"
    
    class Meta:
        db_table = "'post'"
