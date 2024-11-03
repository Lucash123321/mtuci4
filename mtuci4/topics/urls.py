from django.urls import path
from topics import views

app_name = "topics"

urlpatterns = [
    path('', views.main, name='main'),
    path('topic/<str:slug>', views.topic, name='topic'),

    path('testtopic/', views.topic, name='test'),
    path('testpost/', views.post, name='post'),
]