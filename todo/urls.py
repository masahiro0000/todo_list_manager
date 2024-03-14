from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todos/', views.todos, name="todos"),
    path('create-todo/', views.create_todo, name="create-todo"),
    path('<int:todo_id>/edit', views.edit, name="edit"),
    path('complete/<int:todo_id>', views.complete, name="complete"),
]