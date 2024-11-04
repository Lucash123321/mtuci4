from django.contrib import admin
from topics import models

# Register your models here.
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
