from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
    '''
    Abstract manager
    '''
    def get_object_by_public_id(self, public_id):
        '''
        Get a user object by public_id
        '''
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        

class AbstractModel(models.Model):
    '''
    Abstract model
    '''
    public_id = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True