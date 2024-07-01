
from django.urls import path

from . import views

urlpatterns = [
    path('todo/', views.ListTodoView.as_view(), name='todo-list'),
    path('todo/<int:pk>/detail/', views.DetailTodoView.as_view(), name='todo-detail'),
    path('todo/create/', views.CreateTodoView.as_view(), name='todo-create'),
    path('todo/<int:pk>/delete/', views.DeleteTodoView.as_view(), name='todo-delete'),
    path('todo/<int:pk>/update/', views.UpdateTodoView.as_view(), name='todo-update'),
]