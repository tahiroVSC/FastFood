# Generated by Django 5.0.1 on 2024-01-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0011_about_page_mini_descriptions4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('profession', models.CharField(max_length=255, verbose_name='Профессия')),
                ('image', models.ImageField(upload_to='Image', verbose_name='Фото')),
                ('review', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Настройка отзывов в странице о нас',
                'verbose_name_plural': 'Настройки отзывов в страницы о нас',
            },
        ),
    ]
