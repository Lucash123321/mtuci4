from django.urls import path, include
from posts import views

app_name = "posts"

urlpatterns = [
    path('create/<int:id>', views.create_post, name='create_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/vote/', views.vote_post, name='vote_post'),
    path('<int:id>/get_user_vote', views.get_user_vote, name='get_user_vote'),
]