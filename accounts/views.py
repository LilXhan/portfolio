from django.shortcuts import render

from django.views.generic import CreateView

from .forms import RegisterUser

# Create your views here.
class RegisterUserView(CreateView):
    template_name = 'registration/register.html'
    form_class =  RegisterUser
    success_url = '/'