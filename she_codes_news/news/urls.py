from django.urls import path
from django.contrib.auth.models import User
from . import views
from django.views.generic.detail import DetailView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name ='newStory'),
    path('category/<str:pk>/', views.CategoryView.as_view(), name='storyCategory'),
    path('author/<str:slug>/', views.StoriesbyAuthor.as_view(), name='storyAuthor'),
    path('category/', views.CategoryListView.as_view(), name='categoryList'),
]
