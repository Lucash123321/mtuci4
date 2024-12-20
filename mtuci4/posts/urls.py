from django.urls import path, include
from posts import views

app_name = "posts"

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]