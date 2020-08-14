from django import forms
from django.forms import ModelForm
from .models import NewsStory

"""
Story form configued to allow front-end upload & updates of NewsStory
To be developed - editing and deleting interface.
"""

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'content', 'author']
        widgets = {
            'image_url': forms.URLField,
            'pub_date': forms.DateInput(
                format=('%m/%d/%y'),
                attrs={ 
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }


# class EditStoryForm(ModelForm):
#     class Meta:
#         model = NewsStory
#         fields = ['title', 'pub_date', 'category', 'content', 'image_url', 'author']
#         widgets = {
#             'image_url': forms.URLField,
#             'pub_date': forms.DateInput(
#                 format=('%m/%d/%y'),
#                 attrs={ 
#                     'class': 'form-control',
#                     'placeholder': 'Select a date',
#                     'type': 'date'
#                 }
#             )
#         }