from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    
    # A timestamp representing when this object was created.
    created = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    lastUpdate = models.DateTimeField(auto_now=True, blank=True, null=True)

    
    def __str__(self):
        return self.username

    def getName(self):
        return self.first_name + " " + self.last_name

