from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'content', 'image_url']
        widgets = {
            # 'image_url': forms.URLField,
            'pub_date': forms.DateInput(
                format=('%m/%d/%y'),
                attrs={ 
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }