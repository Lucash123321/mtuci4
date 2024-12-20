from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password


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

@login_required
def settings(request):
    if request.method == "POST":
        user = request.user
        new_username = request.POST.get("login", "").strip()
        new_password = request.POST.get("password", "").strip()

        # Проверка имени пользователя
        if new_username:
            if CustomUser.objects.filter(username=new_username).exclude(pk=user.pk).exists():
                messages.error(request, "Имя пользователя уже занято.")
                return redirect('users:settings')
            user.username = new_username

        # Проверка пароля
        if new_password and len(new_password) > 0:
            if len(new_password) < 8:
                messages.error(request, "Пароль должен быть не менее 8 символов.")
                return redirect('users:settings')
            user.password = make_password(new_password)

        user.save()
        return redirect('users:profile')

    return render(request, 'users/settings.html')

def logout(request):
    auth_logout(request)
    return redirect('main')
