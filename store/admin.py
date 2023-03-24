from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description', 'created_at')
    prepopulated_fields = {'slug': ('name',)}

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_name', 'size')


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('fname',)
    list_display = (
        'id',
        'status',
        'fname',
        'lname',
        'phone',
        'address',
        'city',
        'total_price',
        'payment_method',
        'created_at')
    list_filter = ['created_at']
    inlines = [OrderItemAdmin]


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gmail', 'number', 'message', 'created_at')


class emailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')


class profileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'phone',
        'address',
        'city',
        'state',
        'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'sender_name',
        'original_price',
        'selling_price',
        'trending',
        'created_at')
    prepopulated_fields = {'slug': ('name',)}

class ProfitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'report_per_day',
        'report_per_week',
        'report_per_month',
        'report_per_season',
        'report_per_year',
        'report_per_all',
        )


class GoodsSoldAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_of_products',
        'how_many_times_sold',
        'item_size',
        'created_at',
        )
    list_filter = ['created_at']

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_clients', 'total_price')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'size', 'quantity')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Сarousel)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Profile, profileAdmin)
admin.site.register(news_email, emailAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Profit, ProfitAdmin)
admin.site.register(GoodsSold, GoodsSoldAdmin)
# admin.site.register(OrderItem, OrderItem_Admin)
# admin.site.register(Cart, Cart_Admin)
# admin.site.register(Order_product, Order_product_admin)
