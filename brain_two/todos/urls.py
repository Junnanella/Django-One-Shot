from django.urls import path
from todos.views import (
    TodoListView,
    TodoListCreateView,
    TodoListDetailView,
    TodoItemCreateView,
    TodoListDeleteView,
    TodoListUpdateView,
    TodoItemUpdateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todolists"),
    path("<int:pk>/", TodoListDetailView.as_view(), name="todolist_detail"),
    path("create/", TodoListCreateView.as_view(), name="todolist_create"),
    path("items/create/", TodoItemCreateView.as_view(), name="todoitem_create"),
    path(
        "<int:pk>/delete/", TodoListDeleteView.as_view(), name="todolist_delete"
    ),
    path(
        "<int:pk>/edit/", TodoListUpdateView.as_view(), name="todolist_update"
    ),
    path(
        "items/<int:pk>/edit/",
        TodoItemUpdateView.as_view(),
        name="todoitem_update",
    ),
]
