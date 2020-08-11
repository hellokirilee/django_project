from django.contrib.auth import get_user_model
from django.views import generic
from django.views.generic import DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import NewsStory, NewsCategory
from .forms import StoryForm
from django.shortcuts import render


User = get_user_model()


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')[4:]
        return context


class StoriesbyAuthor(generic.DetailView):
    template_name = 'news/storyAuthor.html'
    model = User
    context_object_name = 'author'
    slug_field = "username"
    #set slug here #then change url to use string #change all url code in templates to use 

class CategoryView(generic.DetailView):
    #This view returns all stories, but allows for filtering by the NewsCategory Class
    model = NewsCategory
    template_name = 'news/storyCategory.html'
    context_object_name = 'category_name'

# """View to edit post"""
# class EditStory(generic,UpdateView):
#     model = NewsStory
#     template_name = "news/storyEdit.html"
#     context_object_name = "selected_story"    


"""View to show list of posts"""
class CategoryListView(ListView):
    template_name = "news/categoryList.html"

    def get_queryset(self):
        '''Return all news categories.'''
        return NewsCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsCategory.objects.order_by('category')
        return context


    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

