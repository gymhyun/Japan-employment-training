from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_main, name='calendar_main'),
    path('todo/<str:date>/', views.todo_list, name='todo_list'),
    path('todo/<str:date>/create/', views.todo_create, name='todo_create'),
    path('todo/<int:todo_id>/toggle/', views.todo_toggle, name='todo_toggle'),
    path('todo/<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]