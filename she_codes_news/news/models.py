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
    category = models.CharField(max_length=50, unique=True, primary_key=True)
    

#this gives a meaningful name in Admin section    
    def __str__(self):
        return self.category
    
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(max_length = 200)
    category = models.ForeignKey(
        NewsCategory,
        on_delete = models.CASCADE,
        related_name = "stories",
        # Can allow null for existing data - but require it on form.
        null = True
    )

    #returns meaningful description in Admin interface
    def __str__(self):
        return str(self.title) + " - " + str(self.category)

