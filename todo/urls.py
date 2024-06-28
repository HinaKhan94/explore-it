from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<slug:slug>/', views.todo_detail, name='todo_detail'),
    path('category/3-6-years/', views.category_3_to_6_years, name='category_3_to_6_years'),
]
