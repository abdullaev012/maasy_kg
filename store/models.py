import datetime
import os
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

from django.db.models import Avg


def get_client_rating(client_id):
    rating = Rating.objects.filter(client_id=client_id).aggregate(
        Avg('rating'))['rating__avg']
    return rating


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Имя категории'
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='Слаг')
    image = models.ImageField(
        upload_to=get_file_path,
        null=True,
        blank=True,
        verbose_name='Изображение Категории')
    description = models.TextField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Описание Категории ')
    status = models.BooleanField(
        default=False,
        verbose_name='Статус Категории ')
    trending = models.BooleanField(
        default=False,
        verbose_name='В тренде')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория')
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Имя товара')
    slug = models.SlugField(
        max_length=150,
        db_index=True,
        verbose_name='Слаг')
    sender_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Отправитель товара')
    product_image = models.ImageField(
        upload_to=get_file_path,
        null=True,
        blank=True,
        verbose_name='Изображение продукта')
    description = models.TextField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Описание')
    first_price = models.FloatField(
        null=False,
        blank=False,
        verbose_name='За сколько вы купили?')
    selling_price = models.FloatField(
        null=False, blank=False, verbose_name='Цена продажи')
    status = models.BooleanField(
        default=False,
        verbose_name='Статус')
    trending = models.BooleanField(
        default=False,
        verbose_name='В тренде')
    tag = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Тег')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавление')

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Size(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Имя товара')
    size = models.PositiveIntegerField(verbose_name='Размер товара')
    quantity = models.PositiveIntegerField(verbose_name='Штук товара')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1)
    size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    orderstatuses = (
        ('В ожидании', 'В ожидании'),
        ('Для доставки', 'Для доставки'),
        ('Заказ отправлен', 'Заказ отправлен'),
    )
    status = models.CharField(
        default='В ожидании',
        max_length=150,
        choices=orderstatuses,
        verbose_name='Статус')
    fname = models.CharField(max_length=150, null=False, verbose_name='Имя')
    # lname = models.CharField(
    #     max_length=150,
    #     null=False,
    #     verbose_name='Фамилия')
    # email = models.CharField(
    #     max_length=150,
    #     null=False,
    #     verbose_name='Электронная почта')
    phone = models.CharField(
        max_length=150,
        null=False,
        verbose_name='Телефон номер')
    address = models.TextField(
        max_length=150,
        null=False,
        verbose_name='Адрес')
    # city = models.CharField(max_length=150, null=False, verbose_name='Город')
    # state = models.CharField(
    #     max_length=150,
    #     null=False,
    #     verbose_name='Область')
    # country = models.CharField(
    #     max_length=150,
    #     null=False,
    #     verbose_name='Страна')
    total_price = models.FloatField(null=False, verbose_name='Итоговая цена')
    payment_method = models.CharField(
        max_length=200, verbose_name='Способ доставки')
    tracking_no = models.CharField(
        null=True,
        max_length=150,
        verbose_name='Номер отслеживания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар')
    price = models.FloatField(null=False, verbose_name='Цена')
    quantity = models.PositiveIntegerField(
        null=False, verbose_name='Количество')
    size = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Размер товара')
    created_at = models.DateTimeField(
        verbose_name='Дата',
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)


    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанный товары'

class Order_product(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь')
    phone = models.CharField(
        max_length=150,
        null=False,
        verbose_name='Телефон номер')
    address = models.TextField(null=False, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def get_rating(self):
        rating = Rating.objects.filter(client=self).aggregate(
            Avg('rating'))['rating__avg']
        return rating


class Сarousel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Карусель', blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='advertisement/')
    created_at = models.DateTimeField(
        verbose_name='Дата',
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_product'
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'


class Contacts(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя', null=False)
    gmail = models.CharField(max_length=150, verbose_name='Е-мейл', null=False)
    number = models.CharField(
        max_length=150,
        verbose_name='Телефон',
        null=False)
    message = models.CharField(
        max_length=150,
        verbose_name='Сообщение',
        null=False)
    created_at = models.DateTimeField(
        verbose_name='Дата',
        auto_now=True,
        auto_now_add=False)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class news_email(models.Model):
    email = models.CharField(max_length=150, verbose_name='Е-мейл', null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    class Meta:
        verbose_name = 'Новый емайл'
        verbose_name_plural = 'Новые емайлы'


class Profit(models.Model):
    report_per_day = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Прибыль за один день')
    report_per_week = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Прибыль за одну неделю')
    report_per_month = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Прибыль за один месяц')
    report_per_season = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Прибыль за один сезон')
    report_per_year = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Прибыль за один год')
    report_per_all = models.PositiveBigIntegerField(
        null=False,
        verbose_name='Все прибыли')

    class Meta:
        verbose_name = 'Прибыль'
        verbose_name_plural = 'Прибыли'


class GoodsSold(models.Model):
    name_of_products = models.CharField(
        max_length=255, verbose_name='Имя товара')
    how_many_times_sold = models.CharField(
        max_length=255, verbose_name='Сколько раз продано')
    item_size = models.CharField(max_length=255, verbose_name='Размер товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    class Meta:
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'


class Rating(models.Model):
    name_of_clients = models.CharField(
        null=False, max_length=255, verbose_name='Имя клиента')
    total_price = models.PositiveIntegerField(
        null=False, verbose_name='Сумма покупки')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
