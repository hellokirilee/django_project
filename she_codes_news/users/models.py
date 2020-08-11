from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass #this is where custom fields could be added

    """As the User/Author is sometimes referred to by username(urls),
    and other times their fullname is displayed, have defined their name in the
    fuction below, rather than way used in the NewsStory app. """
    
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
