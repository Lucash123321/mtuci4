from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


# Create your views here.
class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

@login_required
def profile(request):
    user = request.user
    context = {
        'profile_user': user,
        'posts': user.posts.all().order_by('-date')
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth_logout(request)
    return redirect('main')
