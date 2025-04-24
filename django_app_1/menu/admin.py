from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    '''Используем TabularInline, потому что эта
    штука поможет показать связанные с моделью Menu
    объекты модели MenuItem в виде таблицы в админке.'''
    model = MenuItem
    extra = 0
    fields = ('title', 'parent', 'url', 'named_url', 'order')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ('name', 'slug')