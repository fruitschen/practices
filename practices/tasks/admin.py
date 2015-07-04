from django.contrib import admin

from .models import Task, TaskPoint, Category

class TaskPointInline(admin.TabularInline):
    model = TaskPoint
    extra = 3

class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskPointInline]

admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskPoint)
