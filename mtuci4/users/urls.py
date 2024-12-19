from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    LoginView,
    LogoutView
)
from users.views import SignUpView

app_name = "users"

urlpatterns = [
    path('sign-up', SignUpView.as_view(template_name="users/signup.html"), name='sign_up'),
    path('login', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
