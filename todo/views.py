from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def todo_detail(request, slug):
    todo = get_object_or_404(Todo, slug=slug)
    related_todos = Todo.objects.filter(category=todo.category).exclude(id=todo.id)[:5]
    
    return render(request, 'todo_detail.html', {
        'todo': todo,
        'related_todos': related_todos,
        'range': range(5),
    })

def category_3_to_6_years(request):
    # Fetch the Category object for "3-6 years"
    category = Category.objects.get(name='ages: 3-6 years')
    
    # Fetch all Todo objects related to this category
    todos = Todo.objects.filter(category=category)
    
    return render(request, 'categories/ages1.html', {'todos': todos})