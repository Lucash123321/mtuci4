from django.contrib import admin
from django.db import models
from posts.models import Post

BLACKLIST_FIELDS = {'topic_post_id',} # Поля, которые мы хотим скрыть при создании в админке

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'topic_post_id', 'date')
    list_filter = ('topic',)
    search_fields = ('title', 'content')
    readonly_fields = ('topic_post_id',)
    
    

    def save_model(self, request, obj, form, change):
        if not obj.topic_post_id:
            max_id = Post.objects.filter(topic=obj.topic).aggregate(models.Max('topic_post_id'))['topic_post_id__max']
            obj.topic_post_id = (max_id or 0) + 1
        super().save_model(request, obj, form, change)
    
    # Чтобы не отображать topic_post_id при создании записи через админку, отоброжение только в уже созданных
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not obj:
            fields = [f for f in fields if f not in BLACKLIST_FIELDS]
        return fields