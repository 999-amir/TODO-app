from django.contrib import admin
from .models import TodoModel


class TodoInline(admin.TabularInline):
    model = TodoModel
    can_delete = True
    extra = 0
