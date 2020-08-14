from django.urls import path
from django.contrib.auth.models import User
from . import views
from django.views.generic.detail import DetailView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #loads an individual story using a numerical key
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    #form to add a new story
    path('add-story/', views.AddStoryView.as_view(), name ='newStory'),
    #stories grouped by category considering value in page with list of
    #categories over something like StoryCard
    path('category/<str:pk>/', views.CategoryView.as_view(), name='storyCategory'),
    #stories grouped by author
    #to be considered, an author profile page
    path('author/<slug:slug>/', views.StoriesbyAuthor.as_view(), name='storyAuthor'),
    #list of story categories - to be called by card maybe??
    path('category/', views.NewsListView.as_view(), name='newsList'),
    #list of stories by authors - to be called by card instead?
    path('author/', views.NewsAuthorListView.as_view(), name='authorList'),
    #not working
    # path('story/<int:pk>/edit/', views.EditStory.as_view(), name='editStory'),
]
