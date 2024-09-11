from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", ) #este es un campo de sólo lectura, no se puede modificar.

# Register your models here.
admin.site.register(Task, TaskAdmin)
