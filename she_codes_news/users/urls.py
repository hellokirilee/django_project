from django.urls import path
from .views import CreateAccountView, UpdateAccountView
app_name = 'users'
urlpatterns = [
    #Create Account link - need to consider how access to this link will be given,
    #consider changing this to just edit account - with users to be set-up in Admin Center
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/update-account/', UpdateAccountView.as_view(), name='updateAccount'),
    ]