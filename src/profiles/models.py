from django.contrib.auth.models import AbstractUser
from django.db import models


class UserBlog(AbstractUser):
    """
    Custom user model
    """
    middle_name = models.CharField('Middle name(Отчество)', max_length=50, null=True)
    first_login = models.DateTimeField('first login', null=True)
    phone = models.CharField('phone', max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
