# Generated by Django 5.0.1 on 2024-01-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide', verbose_name='Фото для слайда')),
            ],
            options={
                'verbose_name': 'Настройка Слайда',
                'verbose_name_plural': 'Настройки Слайда',
            },
        ),
    ]
