from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
#confirm if needed
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here - looking to update this with edit account only
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'



# class UpdateAccountView(generic.UpdateView):
#     form_class = CustomChangeForm
#     template_name = 'users/updateAccount.html'
#     context_object_name = 'User'
#     #change to view of profile later?
#     success_url = reverse_lazy('news:index')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form) 