from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Role


class CustomUser(AbstractUser):
    ip = models.CharField(max_length=15)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)
    