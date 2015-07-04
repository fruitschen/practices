from django.contrib import admin

from .models import Task, TaskPoint, Category

class TaskPointInline(admin.TabularInline):
    model = TaskPoint
    extra = 3

class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskPointInline]
    list_display = ['priority', 'name', 'finished', ]
    list_filter = ['priority', 'taskpoint__category', 'finished', ]

admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskPoint)
