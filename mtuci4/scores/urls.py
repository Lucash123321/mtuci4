from django.urls import path, include
from scores import views

app_name = "scores"

urlpatterns = [
    path('scores/get/<str:parent_type>/<int:id>', views.get_scores, name='get_scores'),
    path('scores/vote/<str:parent_type>/<int:id>', views.vote_scores, name='vote_scores'),
]