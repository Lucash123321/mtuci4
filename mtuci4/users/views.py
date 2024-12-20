from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


# Create your views here.
class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
    
def profile(request):
    pass

def logout(request):
    auth_logout(request)
    return redirect('main')
