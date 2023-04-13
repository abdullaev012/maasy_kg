from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'slug', 'description', 'created_at')
    prepopulated_fields = {'slug': ('name',)}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'size')


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('fname',)
    list_display = (
        'fname',
        'lname',
        'phone',
        'address',
        'city',
        'total_price',
        'status',
        'payment_method',
        'created_at')
    list_editable = ['status']
    list_filter = ['created_at']
    inlines = [OrderItemAdmin]


class ContactsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'gmail', 'number', 'message', 'created_at')


class emailAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email', 'created_at')


class profileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'address',
        'city',
        'state',
        'created_at')
    search_fields = ('user', 'phone', 'address')
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'sender_name',
        'first_price',
        'selling_price',
        'trending',
        'created_at')
    search_fields = ('name',)
    list_editable = ['first_price', 'selling_price', 'trending']
    prepopulated_fields = {'slug': ('name',)}

class ProfitAdmin(admin.ModelAdmin):
    list_display = (
        'report_per_day',
        'report_per_week',
        'report_per_month',
        'report_per_season',
        'report_per_year',
        'report_per_all',
        )


class GoodsSoldAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_products',
        'how_many_times_sold',
        'item_size',
        'created_at',
        )
    search_fields = ('name_of_products',)
    list_filter = ['created_at']

class RatingAdmin(admin.ModelAdmin):
    search_fields = ('name_of_clients',)
    list_display = ('name_of_clients', 'total_price')


class SizeAdmin(admin.ModelAdmin):
    search_fields = ('product',)
    list_display = ('product', 'size', 'quantity')
    list_editable = ['size', 'quantity']

class СarouselAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Сarousel, СarouselAdmin)
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
