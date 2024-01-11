# Generated by Django 5.0.1 on 2024-01-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Begin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Навзание товара')),
                ('price', models.CharField(max_length=255, verbose_name='Цена со скидкой')),
                ('price_discount', models.CharField(max_length=255, verbose_name='Цена без скидки')),
            ],
            options={
                'verbose_name': 'Дополнительна настройка',
                'verbose_name_plural': 'Дополнительные настройки',
            },
        ),
    ]
