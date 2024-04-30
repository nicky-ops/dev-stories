from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    """
    This class extends the User model and provides additional fields. Has a one-to-one relationship with the Django User model.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'