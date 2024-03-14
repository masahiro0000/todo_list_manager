from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ToDoForm
from .models import Todo

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
def edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = ToDoForm(instance=todo)
    context = {
        "form": form,
        "todo": todo,
    }
    return render(request, "edit.html", context)

@login_required
@require_POST
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todos')

@login_required
@require_POST
def complete(request, todo_id):
    #ToDoの完了のチェックボックスをつける
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed #完了、未完了を反転させる
    todo.save()
    return redirect('todos')