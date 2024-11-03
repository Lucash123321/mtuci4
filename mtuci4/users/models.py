from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser():
    role = models.CharField(max_length=50, blank=True, null=True)
    