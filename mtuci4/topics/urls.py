from django.urls import path
from topics import views

app_name = "topics"

urlpatterns = [
    path('', views.main, name='index'),
    path('testtopic/', views.topic, name='test'),
    path('testpost/', views.post, name='post'),

    path('<str:slug>', views.topic, name='topic'),
]