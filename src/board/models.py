from django.db import models
from src.profiles.models import Technology
from config import settings


class Project(models.Model):
    """ Model project """
    project_name = models.CharField('Название проекта', max_length=250)
    project_preview = models.ImageField('Картинка проекта', upload_to='project/preview/', blank=True, null=True)
    project_description = models.TextField('Описание проекта', blank=True, null=True)
    project_github = models.CharField("Ссылка github проекта", max_length=500, blank=True, null=True)
    project_technology = models.ManyToManyField(Technology, related_name='project')
    project_date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    project_published = models.BooleanField(default=True)
    project_view_count = models.IntegerField('Просмотры проекта', default=0)
    project_user_creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                             on_delete=models.CASCADE,
                                             related_name='project')

    def __str__(self):
        return self.project_name
