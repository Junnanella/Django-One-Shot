from django.urls import path
from todos.views import (
    TodoListView,
    TodoListCreateView,
    TodoListDetailView,
    TodoItemCreateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todolists"),
    path("<int:pk>/", TodoListDetailView.as_view(), name="todolist_detail"),
    path("create/", TodoListCreateView.as_view(), name="todolist_create"),
    path("items/create/", TodoItemCreateView.as_view(), name="todoitem_create"),
]
