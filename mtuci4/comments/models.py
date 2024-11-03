from django.db import models

# Create your models here.
class Comment(models.Model):
    #  author = models.ForeignKey(User, related_name=comment_author, on_delete=model.CASCADE)
    text = models.TextField()
