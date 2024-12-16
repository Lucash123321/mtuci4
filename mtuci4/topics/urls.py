from django.urls import path, include
from topics import views

app_name = "topics"

urlpatterns = [
    path('<str:slug>', views.topic, name='topic'),
    path('<str:topic_slug>/posts/', include("posts.urls", namespace='posts')),
]