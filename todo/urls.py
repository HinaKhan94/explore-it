from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<slug:slug>/', views.todo_detail, name='todo_detail'),
]
