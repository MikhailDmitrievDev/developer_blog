from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import UserBlog
from .serializers import GetUserBlogSerializer, GetPublicUserBlogSerializer


class PublicUserBlogView(ModelViewSet):
    """Public user view"""
    queryset = UserBlog.objects.all()
    serializer_class = GetPublicUserBlogSerializer
    permission_classes = [permissions.AllowAny]

class UserBlogView(ModelViewSet):
    """Private user view."""
    serializer_class = GetUserBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserBlog.objects.filter(id=self.request.user.id)