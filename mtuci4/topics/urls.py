from django.urls import path
from topics import views

app_name = "topics"

urlpatterns = [
    path('', views.main, name='index'),
]