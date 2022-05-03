from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
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

    def form_invalid(self, form):
        context = super().form_invalid(form)

    success_url = reverse_lazy("todos/todo_lists.html")


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/todolist_detail.html"


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todos/todoitem_create.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def form_invalid(self, form):
        context = super().form_invalid(form)

    success_url = reverse_lazy("todos/todo_lists.html")
