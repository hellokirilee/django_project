from django.contrib.auth import get_user_model
from django.views import generic
from django.views.generic import DetailView, UpdateView, ListView, CreateView  
from django.urls import reverse_lazy
from .models import NewsStory, NewsCategory
from .forms import StoryForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import UserPassesTestMixin


User = get_user_model()

"""News 'home' page"""
class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')[4:6]
    
        return context

"""view for individual story page"""
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"


"""View to post a new story"""
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


# """View to edit post"""
# class EditStory(generic.UpdateView):
#     form_class = EditStoryForm
#     model = NewsStory
#     context_object_name = 'storyForm'
#     template_name = 'news/editStory.html'
#     success_url = reverse_lazy('news:index')

#     # def form_valid(self, form):
#     #     author=self.request.user
#     #     form.instance.author = self.request.user
#     #     return super().form_valid(form)
#     # return False

#     def is_author(self,user):
#         author = self.request.user
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#     def test_func(self):
#             story = self.get_object()
#             if self.request.user == story.author:
#                 return True

        





"""Context Object name is used to call in templates"""

class StoriesbyAuthor(generic.DetailView):
    model = User
    template_name = 'news/storyAuthor.html'
    context_object_name = 'author_name'
    slug_field = "username"
    #set slug here #then change url to use string #change all url code in templates to use 

class CategoryView(generic.DetailView):
    #This view returns all stories, but allows for filtering by the NewsCategory Class
    model = NewsCategory
    template_name = 'news/storyCategory.html'
    context_object_name = 'category_name'



"""View to show list of posts"""
class NewsListView(ListView):
    template_name = "news/categoryList.html"

    def get_queryset(self):
        '''Return all news categories.'''
        return NewsCategory.objects.all(), User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = NewsCategory.objects.order_by('category')
        context['all_authors'] = User.objects.order_by('last_name')
        return context

class NewsAuthorListView(ListView):
    template_name = "news/authorList.html"

    def get_queryset(self):
        '''Return all news categories.'''
        return NewsCategory.objects.all(), User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        context['all_authors'] = User.objects.order_by('last_name')
        return context