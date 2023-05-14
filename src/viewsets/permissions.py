from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsMemberTeam(BasePermission):
    """ Участник команды """
    pass


class IsAuthorProject(BasePermission):
    """ Автор проекта или администратор """
    def has_object_permission(self, request, view, obj):
        return obj.project_user_creator == request.user or obj.entry.group.founder == request.user
