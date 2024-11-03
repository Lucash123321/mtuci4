from django.db import models
from topics.models import Topic

# Create your models here.
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptiomn = models.TextField()
