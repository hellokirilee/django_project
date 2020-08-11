from django.contrib import admin
from .models import NewsStory, NewsCategory
# Register your models here.
"""Each time a new model is added to Admin:
- update import
- ensure that NewsAdmin is updated with user friendly formatting """

"""This Class is used to improve layout and view of the Admin Center Story View
New Category has been set up as a simple field, so changes are not necessary"""
class NewsAdmin(admin.ModelAdmin):
    list_filter = ['author', 'category']
    list_display = ['title', 'category', 'author', 'pub_date']

    fieldsets = [
        ('Details', {'fields': ['title', 'category', 'author', 'pub_date']}),
        ('Content', {'fields': ['content', 'image_url']}),
    ]


admin.site.register(NewsStory, NewsAdmin)
admin.site.register(NewsCategory)
