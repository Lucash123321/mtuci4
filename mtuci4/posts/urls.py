from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
    path('topic/<slug:topic_slug>/posts/create/', views.create_post, name='create_post'),
    path('topic/<slug:topic_slug>/posts/<int:id>/', views.post_detail, name='post_detail'),
    path('topic/<slug:topic_slug>/posts/<int:id>/vote/<str:vote_type>/', views.vote_post, name='vote_post'),
    path('topic/<slug:topic_slug>/posts/<int:id>/comment/', views.create_comment, name='add_comment'),
]