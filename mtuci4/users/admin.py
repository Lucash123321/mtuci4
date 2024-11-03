from django.contrib import admin
from users import models

# Register your models here.
@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    exclude = ('email', 'first_name', 'last_name')
