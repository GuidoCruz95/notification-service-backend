from django.contrib import admin

from .models import Category, GilaMessage, Channel, User, LogHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(GilaMessage)
class GilaMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'category')


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('description', 'type')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')


@admin.register(LogHistory)
class LogHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'user', 'channel')
