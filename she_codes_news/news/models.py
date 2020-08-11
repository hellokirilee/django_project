from django.contrib.auth import get_user_model
from django.db import models

"""
Things to Remember when adding or updating models!
Add Model - makemigrations/migrate
Add Views - Import if needed
Add URLS - Import if needed
Update Admin Page - Import if needed
Add Template
Update existing Templates
Consider Forms
"""

class NewsCategory (models.Model):
#Categories have been defined with their name as pk.
#Duplicates will now be alloed, and SuperUsers can add additional Categories behind the by logging in.
    category = models.CharField(max_length=50, unique=True, primary_key=True)
    """verbose name & verbose plural name act as display names, 
    providing formatting when called by forms, or in the admin center 
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    """related_name is what this model is called when
    referred to from the other model
    """
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "stories"
    )
    pub_date = models.DateField(verbose_name = 'Date Publised')
    content = models.TextField()
    image_url = models.URLField(max_length = 200, verbose_name = 'Image URL')
    category = models.ForeignKey(
        NewsCategory,
        on_delete = models.CASCADE,
        related_name = "stories",
        # Can allow null for existing data - but require it on form.
        null = True
    )
    """verbose name & verbose plural name act as display names, 
    providing formatting when called by forms, or in the admin center 
    """
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    """ 
    This sets the default field when the NewsStory is called.
    Currently set to just title - but alternatiely, can be set to return a string
    of self.title " "+" " self.category
    """
    def __str__(self):
          return self.title