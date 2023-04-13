# Generated by Django 4.1.7 on 2023-04-13 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Слаг')),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path, verbose_name='Изображение Категории')),
                ('description', models.TextField(max_length=500, verbose_name='Описание Категории ')),
                ('status', models.BooleanField(default=False, verbose_name='Статус Категории ')),
                ('trending', models.BooleanField(default=False, verbose_name='В тренде')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('gmail', models.CharField(max_length=150, verbose_name='Е-мейл')),
                ('number', models.CharField(max_length=150, verbose_name='Телефон')),
                ('message', models.CharField(max_length=150, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='GoodsSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_products', models.CharField(max_length=255, verbose_name='Имя товара')),
                ('how_many_times_sold', models.CharField(max_length=255, verbose_name='Сколько раз продано')),
                ('item_size', models.CharField(max_length=255, verbose_name='Размер товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
            },
        ),
        migrations.CreateModel(
            name='news_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='Е-мейл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Новый емайл',
                'verbose_name_plural': 'Новые емайлы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('В ожидании', 'В ожидании'), ('Для доставки', 'Для доставки'), ('Заказ отправлен', 'Заказ отправлен')], default='В ожидании', max_length=150, verbose_name='Статус')),
                ('fname', models.CharField(max_length=150, verbose_name='Имя')),
                ('lname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=150, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=150, verbose_name='Телефон номер')),
                ('address', models.TextField(max_length=150, verbose_name='Адрес')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('state', models.CharField(max_length=150, verbose_name='Область')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('total_price', models.FloatField(verbose_name='Итоговая цена')),
                ('payment_method', models.CharField(max_length=200, verbose_name='Способ доставки')),
                ('tracking_no', models.CharField(max_length=150, null=True, verbose_name='Номер отслеживания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя товара')),
                ('slug', models.SlugField(max_length=150, verbose_name='Слаг')),
                ('sender_name', models.CharField(max_length=150, verbose_name='Отправитель товара')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path, verbose_name='Изображение продукта')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('first_price', models.FloatField(verbose_name='За сколько вы купили?')),
                ('selling_price', models.FloatField(verbose_name='Цена продажи')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('trending', models.BooleanField(default=False, verbose_name='В тренде')),
                ('tag', models.CharField(max_length=150, verbose_name='Тег')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_per_day', models.PositiveBigIntegerField(verbose_name='Прибыль за один день')),
                ('report_per_week', models.PositiveBigIntegerField(verbose_name='Прибыль за одну неделю')),
                ('report_per_month', models.PositiveBigIntegerField(verbose_name='Прибыль за один месяц')),
                ('report_per_season', models.PositiveBigIntegerField(verbose_name='Прибыль за один сезон')),
                ('report_per_year', models.PositiveBigIntegerField(verbose_name='Прибыль за один год')),
                ('report_per_all', models.PositiveBigIntegerField(verbose_name='Все прибыли')),
            ],
            options={
                'verbose_name': 'Прибыль',
                'verbose_name_plural': 'Прибыли',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_clients', models.CharField(max_length=255, verbose_name='Имя клиента')),
                ('total_price', models.PositiveIntegerField(verbose_name='Сумма покупки')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Сarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Карусель')),
                ('image', models.ImageField(upload_to='advertisement/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусели',
                'db_table': 'advertisement_product',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveIntegerField(verbose_name='Размер товара')),
                ('quantity', models.PositiveIntegerField(verbose_name='Штук товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Имя товара')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=150, verbose_name='Телефон номер')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('state', models.CharField(max_length=150, verbose_name='Область')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('size', models.CharField(max_length=150, verbose_name='Размер товара')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказанный товар',
                'verbose_name_plural': 'Заказанный товары',
            },
        ),
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('size', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
