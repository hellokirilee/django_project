from django.contrib import admin
from .models import NewsStory, NewsCategory
# Register your models here.
"""Each time a new model is added to Admin:
- update import
- ensure that models.py is updated with user friendly formatting """
admin.site.register(NewsStory)
admin.site.register(NewsCategory)

#username: admin password: admin