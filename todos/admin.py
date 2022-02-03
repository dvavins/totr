from atexit import register
from sqlite3 import register_adapter
import django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'todo_date', 'is_completed')
    list_display_links = ('name', 'user')

    search_fields = ('name', 'desc',)
    readonly_fields = ('date_created', 'slug')
    list_filter = ('user',)
    filter_horizontal = ()
    
    fieldsets = (
        (_('Task Details'), {'fields': ('user',)}),
        (_('Todo Details'), {'fields': ('name', 'slug', 'desc')}),
        (_('Important dates'), {'fields': ('todo_date', 'date_created')}),
        (_('Status'), {'fields': ('is_completed', )}),
    )


admin.site.register(Todos, TodosAdmin)