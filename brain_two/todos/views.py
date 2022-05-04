from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)
from todos.models import TodoItem, TodoList
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos/todo_lists.html"


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/todolist_create.html"
    fields = ["name"]

    def form_valid(self, form):
        todolist = form.save(commit=False)
        todolist.save()
        return redirect("todolist_detail", pk=todolist.id)


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/todolist_detail.html"


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/todolist_delete.html"

    success_url = reverse_lazy("todolists")


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/todolist_update.html"
    fields = ["name"]

    def form_valid(self, form):
        todolist = form.save(commit=False)
        todolist.save()
        return redirect("todolist_detail", pk=todolist.id)


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todos/todoitem_create.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def form_valid(self, form):
        todoitem = form.save(commit=False)
        todoitem.save()
        return redirect("todolist_detail", pk=todoitem.id)


class TodoItemUpdateView(UpdateView):
    model = TodoItem
    template_name = "todos/todoitem_update.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def form_valid(self, form):
        todoitem = form.save(commit=False)
        todoitem.save()
        return redirect("todolist_detail", pk=todoitem.id)
