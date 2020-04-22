from django.contrib import admin
from .models import Project, Resume
from todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)


admin.site.register(Project)

admin.site.register(Resume)
