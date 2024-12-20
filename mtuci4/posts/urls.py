from django.urls import path, include
from posts import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('<str:topic_slug>/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('<str:topic_slug>/delete/<int:post_id>', views.delete_post, name='delete_post'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('', views.check_permission, name='check_permission'),
]