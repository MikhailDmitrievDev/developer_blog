from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Проекты"""
    list_display = ("project_name", "project_preview", "project_description",
                    "project_github", "project_date_create",
                    "project_published", "project_view_count", "project_user_creator")