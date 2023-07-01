from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

class LoginView(BaseLoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy('todo:list')
      
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('todo:list')
    
class LogoutView(BaseLogoutView):
    template_name = "registration/logout.html"
    success_url = reverse_lazy('todo:list')