from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required
from .forms import ToDoForm

def index(request):
    return render(request, "index.html")

@login_required
def todos(request):
    #作成日順にユーザーのタスクを取得
    user_todos = Todo.objects.filter(user = request.user).order_by("created_at")

    context = {"user_todos" : user_todos}
    return render(request, "todos.html", context)

@login_required
def create_todo(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos')
    else:
        form = ToDoForm()
    return render(request, "create_todo.html", {"form": form})

@login_required
def complete(request, todo_id):
    #ToDoの完了のチェックボックスをつける
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed #完了、未完了を反転させる
    todo.save()
    return redirect('todos')