from django.contrib import admin
from roles.models import Permission, Role

# Register your models here.


@admin.register(Permission)
class PostAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    search_fields = ('role', )


@admin.register(Role)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
