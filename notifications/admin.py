from django.contrib import admin
from .models import Category, Message


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'category')
