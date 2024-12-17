from django.db import models
from django.conf import settings
from posts.models import Post
from django.core.exceptions import ValidationError

# Create your models here.
class Comment(models.Model):
    # Может быть либо только post, тогда parent = None, либо только parent, тогда post = None.
    # Таким образом можно реализовать вложенность двойного уровня без лишних костылей.
    
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True, blank=True,)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user} on {self.post}" if not self.parent else f"Reply by {self.user}"

    @property
    def is_reply(self):
        return self.parent is not None
    
    def clean(self):
        # Проверка, что только одно из полей заполнено: либо post, либо parent.
        if self.post and self.parent:
            raise ValidationError("Не может быть заполнено сразу два поля: 'post' и 'parent'.")
        if not self.post and not self.parent:
            raise ValidationError("Одно из полей должно быть заполнено: 'post' или 'parent'.")
    
    # Для максимального уровня вложенности в виде ответа на комментарий (как в ВК короче)
    def save(self, *args, **kwargs):
        # Если у комментария есть родитель, который не Post (тогда это ответ на какой-то комментарий)
        if self.parent:
            # Если родитель имеет родителя (вложенность больше 1), переопределяем родителя
            if self.parent.parent:
                self.parent = self.parent.parent
                
        super().save(*args, **kwargs)
    
    