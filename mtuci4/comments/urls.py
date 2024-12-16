from django.urls import path
from comments import views

app_name = "comments"

urlpatterns = [
    path('create/', views.create_comment, name='create_comment'),
    path('<int:id>/vote/<str:vote_type>/', views.vote_comment, name='vote_comment')
]