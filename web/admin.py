from django.contrib import admin

from web.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')
    list_filter = ('title',)
    search_fields = ['title']