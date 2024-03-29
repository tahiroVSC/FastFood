# Generated by Django 5.0.1 on 2024-01-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0012_reviews_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='Image', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Настройка новостей',
                'verbose_name_plural': 'Настройки новостей',
            },
        ),
    ]
