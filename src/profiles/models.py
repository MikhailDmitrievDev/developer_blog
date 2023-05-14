from django.contrib.auth.models import AbstractUser
from django.db import models


class UserBlog(AbstractUser):
    """
    Custom user model
    """
    GENDER_CHOICE = (
        ('male', 'male'),
        ('female', 'female')
    )
    middle_name = models.CharField('Отчество', max_length=50, null=True)
    first_login = models.DateTimeField('Первый вход', blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=14)
    avatar = models.ImageField('Аватар пользователя', upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField('Биография', blank=True, null=True)
    github = models.CharField('Ссылка github', max_length=500, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField('Пол', max_length=6, choices=GENDER_CHOICE, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    """Модель технологий"""
    name = models.CharField('Имя технологии.', max_length=200)

    def __str__(self):
        return self.name

