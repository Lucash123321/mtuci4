from django.contrib import admin
from comments.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'date', 'parent')
    list_filter = ('date',)
    ordering = ('-date',)
    search_fields = ('content',)
    