from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Begin(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Навзание товара"
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = "Цена со скидкой"
    )
    price_discount = models.CharField(
        max_length = 255,
        verbose_name = "Цена без скидки"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка начало'
        verbose_name_plural = 'Настройки начало'

class About(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    descriptions2 = models.TextField(
        verbose_name = "Описание"
    )
    customers = models.CharField(
        max_length = 255,
        verbose_name = "Всего клиентов"
    )
    qutlet = models.CharField(
        max_length = 255,
        verbose_name = "Всемирная торговая точка"
    )
    satisfaction = models.CharField(
        max_length = 255,
        verbose_name = "Удовлетворение"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройкка о нас"
        verbose_name_plural = "Настройки о нас"

class Category(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройкка котегории"
        verbose_name_plural = "Настройки котегории"
    
class Products(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    imgae = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    price = models.CharField(
        max_length =255,
        verbose_name ="Цена"
    )
    price_discount = models.CharField(
        max_length = 255,
        verbose_name = "Цена без скидки"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка продукты"
        verbose_name_plural = "Настройки продуктов"

class Offer(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = "Цена"
    )
    price_dicount = models.CharField(
        max_length = 255,
        verbose_name = "Цена без скидки"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name = "Фото"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка предложений"
        verbose_name_plural = "Настройки предложений"

class Reviews(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "ФИО"
    )
    descriptions = models.TextField(
        verbose_name = "Отыв"
    )
    profession = models.CharField(
        max_length = 255,
        verbose_name ="Профессия"
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка Отзыва"
        verbose_name_plural = "Настройки Отзывов"

class Blog(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название поста"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    created_at = models.DateField(
        auto_now_add = True,
        blank = True, null = True
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка новостей в Index"
        verbose_name_plural = "Настройки новостей index"

class Slide(models.Model):
    image = models.ImageField(
        upload_to="slide",
        verbose_name="Фото для слайда"
    )
    class Meta:
        verbose_name = "Настройка Слайда"
        verbose_name_plural = "Настройки Слайда"

class About_page(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    experience = models.CharField(
        max_length = 255,
        verbose_name = "Опыт работы"
    )
    mini_descriptions = models.CharField(
        max_length = 255,
        verbose_name = "Мини описание 1"
    )
    mini_descriptions2 = models.CharField(
        max_length = 255,
        verbose_name = "Мини описание 2"
    )
    mini_descriptions3 = models.CharField(
        max_length = 255,
        verbose_name = "Мини описание 3"
    )
    mini_descriptions4 = models.CharField(
        max_length = 255,
        verbose_name = "Мини описание 4"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка страницы о нас"
        verbose_name_plural = "Настройки страницы о нас"

class Reviews_2(models.Model):
    name = models.CharField(
        max_length= 255,
        verbose_name = "ФИО"
    )
    profession = models.CharField(
        max_length =255,
        verbose_name = "Профессия"
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    review = models.TextField(
        verbose_name = "Отзыв"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка отзывов в странице о нас"
        verbose_name_plural = "Настройки отзывов в страницы о нас"


class Blogs(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название поста"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    created_at = models.DateField(
        auto_now_add = True,
        blank = True, null = True
    )
    image = models.ImageField(
        upload_to="Image",
        verbose_name="Фото"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка новостей"
        verbose_name_plural = "Настройки новостей"


class Shops(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length =255,
        verbose_name = "Навзание"
    )
    image = models.ImageField(
        upload_to= "Image",
        verbose_name="Фото"
    )
    price = models.CharField(
        max_length =255,
        verbose_name = "Цена"
    )
    price_discount = models.CharField(
        max_length = 255,
        verbose_name = "Цена без скидки"
    )
    discriptions = models.TextField(
        verbose_name = "Описание"
    )
    discriptions_mini = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка Магазина"
        verbose_name_plural = "Настройки Магазина"

class MilkShake(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='milk_shake', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Молочный коктель'
        verbose_name_plural = 'Молочные коктели'



class FructJuice(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='fruct_juice/', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фруктовый коктель'
        verbose_name_plural = 'Фруктовые коктели'


class IceCreame(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='ice_creame', verbose_name='Фото')
    price = models.CharField(max_length=255, verbose_name='Цена')
    disc = models.TextField(verbose_name='описание')