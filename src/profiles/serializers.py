from rest_framework import serializers

from .models import UserBlog


class GetUserBlogSerializer(serializers.ModelSerializer):
    """ Вывод инофрмации о пользователе"""
    class Meta:
        model = UserBlog
        exclude = ("password",
                   "last_login",
                   "is_active",
                   "is_staff",
                   "is_superuser")

class GetPublicUserBlogSerializer(serializers.ModelSerializer):
    """Публичный вывод информации о пользователе."""
    class Meta:
        model = UserBlog
        exclude = ("password",
                   "is_active",
                   "is_staff",
                   "is_superuser",
                   "email",
                   "phone",
                   "user_permissions")
