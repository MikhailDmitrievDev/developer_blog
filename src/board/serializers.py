from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """ Вывод и редактирование проекта
    """
    project_user_creator = serializers.ReadOnlyField(source="project_user_creator.username")

    class Meta:
        model = Project
        project_view_count = serializers.ReadOnlyField()
        fields = ("project_name", "project_preview", "project_description",
                  "project_github", "project_technology", "project_date_create",
                  "project_published", "project_view_count", "project_user_creator",)


class ListProjectSerializer(serializers.ModelSerializer):
    """ Список проектов
    """
    project_user_creator = serializers.ReadOnlyField(source="project_user_creator.username")

    class Meta:
        model = Project
        fields = ("project_name", "project_preview", "project_description",
                  "project_technology", "project_date_create", "project_view_count",
                  "project_user_creator")
