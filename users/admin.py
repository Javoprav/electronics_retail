from django.contrib import admin
from .models import User


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    """Админка для отображения User"""
    list_display = ('id', 'email', 'phone', 'is_active',)
    list_filter = ('id',)
