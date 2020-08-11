from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass #this is where custom fields could be added

    
    #this gives a meaningful name in User model name, viewed in the story view & Admin section
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
