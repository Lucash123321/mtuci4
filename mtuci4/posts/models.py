from django.db import models
from topics.models import Topic

# Create your models here.
class Post(models.Model):
    #  author = models.ForeignKey(User, related_name=post_author, on_delete=model.CASCADE)
    topic = models.ForeignKey(Topic, related_name="post_topic", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptiomn = models.TextField()
