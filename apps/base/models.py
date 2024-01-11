from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = ' Название'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    logo = models.ImageField(
        upload_to='logo_image',
        verbose_name='Логотип1'
    )
    logo2 = models.ImageField(
        upload_to='logo_image',
        verbose_name='Логотип2'
    )
    locations = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес',
        blank =True, null=True
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона',
        blank =True, null=True
    )
    email = models.EmailField(
        verbose_name = 'Почта',
        blank =True, null=True
    )
    instagram = models.URLField(
        verbose_name = 'Инстаграм',
        blank =True, null=True
    )
    twitter = models.URLField(
        verbose_name = 'twitter',
        blank =True, null=True
    )
    youtube = models.URLField(
        verbose_name = 'Ютуб',
        blank =True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'