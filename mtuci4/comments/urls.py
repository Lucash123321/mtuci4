from django.urls import path
from comments import views

app_name = "comments"

urlpatterns = [
    path('create/', views.create_comment, name='create_comment'),
    path('edit/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('<int:id>/vote/<str:vote_type>/', views.vote_comment, name='vote_comment'),
    path('', views.check_permission, name='check_permission'),
]