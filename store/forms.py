from datetime import datetime, timedelta

from django import forms
from django.contrib.auth.forms import UserCreationForm

from store.models import *

from .models import User


class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-2',
                'placeholder': 'Введите имя пользователя'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-2',
                'placeholder': 'Введите номер телефона'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control my-2',
                'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control my-2',
                'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']


def send_report():
    order_item1 = OrderItem.objects.filter(
        created_at__gte=datetime.datetime.now() - timedelta(days=1))
    total1 = []
    for i1 in order_item1:
        total1.append(i1.product.selling_price - i1.product.first_price)

    order_item7 = OrderItem.objects.filter(
        created_at__gte=datetime.datetime.now() - timedelta(days=7))
    total7 = []
    for i7 in order_item7:
        total7.append(i7.product.selling_price - i7.product.first_price)

    order_item30 = OrderItem.objects.filter(
        created_at__gte=datetime.datetime.now() - timedelta(days=30))
    total30 = []
    for i30 in order_item30:
        total30.append(i30.product.selling_price - i30.product.first_price)

    order_item120 = OrderItem.objects.filter(
        created_at__gte=datetime.datetime.now() - timedelta(days=120))
    total120 = []
    for i120 in order_item120:
        total120.append(i120.product.selling_price - i120.product.first_price)

    order_item365 = OrderItem.objects.filter(
        created_at__gte=datetime.datetime.now() - timedelta(days=365))
    total365 = []
    for i365 in order_item365:
        total365.append(i365.product.selling_price - i365.product.first_price)

    order_item_all = OrderItem.objects.all()
    total_all = []
    for i in order_item_all:
        total_all.append(i.product.selling_price - i.product.first_price)

    profit = Profit.objects.all()
    profit.delete()

    profit = Profit()
    total_price = []
    total_price.append(sum(total1))
    total_price.append(sum(total7))
    total_price.append(sum(total30))
    total_price.append(sum(total120))
    total_price.append(sum(total365))
    total_price.append(sum(total_all))
    profit.report_per_day = total_price[0]
    profit.report_per_week = total_price[1]
    profit.report_per_month = total_price[2]
    profit.report_per_season = total_price[3]
    profit.report_per_year = total_price[4]
    profit.report_per_all = total_price[5]
    profit.save()
    print(total_price)


# def goods_sold():
#     order_item1 = OrderItem.objects.filter(
#         created_at__gte=datetime.datetime.now() - timedelta(days=1))
#     total1 = []
#     for i1 in order_item1:
#         total1.append(i1.product.name)
#         total1.append(i1.quantity)
#         total1.append(i1.size)

#     order_item7 = OrderItem.objects.filter(
#         created_at__gte=datetime.datetime.now() - timedelta(days=7))
#     total7 = []
#     for i7 in order_item7:
#         total7.append(i7.product.name)
#         total7.append(i7.quantity)
#         total7.append(i7.size)

#     order_item30 = OrderItem.objects.filter(
#         created_at__gte=datetime.datetime.now() - timedelta(days=30))
#     total30 = []
#     for i30 in order_item30:
#         total30.append(i30.product.name)
#         total30.append(i30.quantity)
#         total30.append(i30.size)

#     order_item120 = OrderItem.objects.filter(
#         created_at__gte=datetime.datetime.now() - timedelta(days=120))
#     total120 = []
#     for i120 in order_item120:
#         total120.append(i120.product.name)
#         total120.append(i120.quantity)
#         total120.append(i120.size)

#     order_item365 = OrderItem.objects.filter(
#         created_at__gte=datetime.datetime.now() - timedelta(days=365))
#     total365 = []
#     for i365 in order_item365:
#         total365.append(i365.product.name)
#         total365.append(i365.quantity)
#         total365.append(i365.size)

#     order_item_all = OrderItem.objects.all()
#     total_all = []
#     for i in order_item_all:
#         total_all.append(i.product.name)
#         total_all.append(i.quantity)
#         total_all.append(i.size)

#     goods_sold = Goods_sold.objects.all()
#     goods_sold.delete()

#     goods_sold = Goods_sold()
#     total_price = []
#     total_price.append(total1)
#     total_price.append(total7)
#     total_price.append(total30)
#     total_price.append(total120)
#     total_price.append(total365)
#     total_price.append(total_all)
#     goods_sold.goods_sold_in_one_day = total_price[0]
#     goods_sold.items_sold_per_week = total_price[1]
#     goods_sold.items_sold_per_month = total_price[2]
#     goods_sold.products_sold_in_one_season = total_price[3]
#     goods_sold.products_sold_in_one_year = total_price[4]
#     goods_sold.all_items_sold = total_price[5]
#     goods_sold.save()
#     # print(total_price)
