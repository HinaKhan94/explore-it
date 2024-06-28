from django.contrib import admin
from .models import Category, Todo, Messages

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('rating', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class MessagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'submission_date',
    )

    ordering = ('submission_date',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Messages, MessagesAdmin)
