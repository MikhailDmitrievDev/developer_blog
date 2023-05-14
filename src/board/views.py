from rest_framework import permissions, generics

from .serializers import ProjectSerializer, ListProjectSerializer
from .models import Project
from src.viewsets.classes import CreateRetrieveUpdateDestroy
from src.viewsets.permissions import IsAuthorProject


class ProjectView(CreateRetrieveUpdateDestroy):
    """ CRUD операции с проектом.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthorProject],
                                    'destroy': [IsAuthorProject]}

    def perform_create(self, serializer):
        serializer.save(project_user_creator=self.request.user)


class ListProjectView(generics.ListAPIView):
    """ Вывод всех проектов пользователя.
    """
    serializer_class = ListProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(project_user_creator_id=self.kwargs.get('pk'))
