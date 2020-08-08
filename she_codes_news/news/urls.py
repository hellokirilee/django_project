from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name ='newStory'),
    path('category/<str:pk>/', views.Category_View.as_view(), name='storyCategory'),
]
