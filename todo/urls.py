from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('my-todo/', views.my_todo, name="my-todo"),
]