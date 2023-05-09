# Generated by Django 4.2.1 on 2023-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userblog',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='userblog',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userblog',
            name='github',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ссылка github'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/avatar/', verbose_name='Аватар пользователя'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Первый вход'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='middle_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Номер телефона'),
        ),
    ]