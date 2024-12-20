
from django.db import models
from users.models import CustomUser


# Create your models here.
class Fingerprint(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fingerprints')
    hashed = models.TextField()
    