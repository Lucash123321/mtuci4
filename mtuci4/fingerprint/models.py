import hashlib
from django.db import models
from users.models import CustomUser


# Create your models here.
class Fingerprint(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    hashed = models.TextField()

    def set_hashed(self, webgl, canvas):
        combined = f"{webgl}{canvas}"
        self.hashed = hashlib.sha256(combined.encode()).hexdigest()