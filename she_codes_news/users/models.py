from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass #this is where I'd put my own fields - __str__ shows how this will display in the Admin page

    def __str__(self):
        return self.username