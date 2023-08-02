from django.contrib import admin

from .models import Category, GilaMessage, LogHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(GilaMessage)
class GilaMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'category')


@admin.register(LogHistory)
class LogHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'user', "message")