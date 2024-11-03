from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
