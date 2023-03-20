from datetime import datetime, timedelta

from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from store.forms import *
from django.db.models import Sum
from store.forms import send_report
from django.db.models import Q
from .models import *


def home(request):
    trending_products = Product.objects.filter(trending=1)
    usual_products = Product.objects.filter(trending=0)
    advertisement = Сarousel.objects.all()
    advertisement_last = Сarousel.objects.last()
    # send_report()
    # goods_sold()

    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True

    orders = Order.objects.all()
    sett = set()
    for i in orders:
        sett.add(i.user.username)

    rating1 = Rating.objects.all()
    rating1.delete()

    for y in sett:
        rating = Rating()
        user1 = User.objects.get(username=y)
        user_orders_sum = Order.objects.filter(user=user1).aggregate(Sum('total_price'))
        rating.name_of_clients = user1.first_name
        rating.total_price = user_orders_sum['total_price__sum']
        rating.save()
        
    dct = {}
    order_item = OrderItem.objects.all()
    for i in order_item:
        if f'{i.product.name}_{i.size}' in dct:
            dct[f'{i.product.name}_{i.size}'] = dct[f'{i.product.name}_{i.size}'] = dct[f'{i.product.name}_{i.size}'] + i.quantity
        else:
            dct[f'{i.product.name}_{i.size}'] = i.quantity
        
    gr = GoodsSold.objects.all()
    gr.delete()
    for f in reversed(dct):
        goodsSold = GoodsSold()
        goodsSold.name_of_products = f
        goodsSold.how_many_times_sold = dct[f]
        goodsSold.item_size = f'{f[-2]+f[-1]}'
        goodsSold.save()

    context = {
        'trending_products': trending_products,
        'advertisement': advertisement,
        'advertisement_last': advertisement_last,
        'usual_products': usual_products,
        'q': q,
        'size_pro': size_pro,
    }
    return render(request, 'index.html', context)


def collections(request):
    category = Category.objects.filter(status=0)
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'category': category, 'q': q}
    return render(request, 'store/collections.html', context)


def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        size_pro = Size.objects.all()
        q = False
        for i in size_pro:
            if i.quantity <= 20:
                q = True
        context = {'products': products, 'category': category, 'q': q}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "Такой категории не найдено")
        return redirect('collections')


@login_required(login_url='loginpage')
def productview(request, cate_slug, prod_slug):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    products_pro = Product.objects.get(slug=prod_slug, status=0)
    size = Size.objects.filter(product=products_pro)
    idd = []
    cart = Cart.objects.filter(user=request.user)
    for i in cart:
        idd.append(i.id)
    id = zip(idd)
    if (Category.objects.get(slug=cate_slug, status=0)):
        if (Product.objects.get(slug=prod_slug, status=0)):
            products = Product.objects.get(slug=prod_slug, status=0)
            context = {'products': products, 'id': id, 'size': size, 'q': q}
        else:
            messages.error(request, "Такой товар не найден")
            return redirect('collections')

    else:
        messages.error(request, "Такой категории не найдено")
        return redirect('collections')
    return render(request, "store/products/view.html", context)


def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productslist = list(products)

    return JsonResponse(productslist, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(
                name__contains=searchedterm).first()

            if product:
                return redirect(
                    'collections/' +
                    product.category.slug +
                    '/' +
                    product.slug)
            else:
                messages.info(
                    request, "Ни один продукт не соответствует вашему запросу")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


def about_us(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True

    context = {'q': q}
    return render(request, "store/about_us.html", context)


def questions(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/questions.html", context)


def orderss(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/for_clients/order.html", context)


def news(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/news.html", context)


def partner(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/bussiness/partner.html", context)


def advertisers(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/bussiness/advertisers.html", context)


def investors(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/bussiness/investors.html", context)


def suppliers(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/bussiness/suppliers.html", context)


def delivery(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/for_clients/delivery.html", context)


def sposob(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/for_clients/sposob.html", context)


def vozvrat(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/for_clients/vozvrat.html", context)


def contacts(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True
    context = {'q': q}
    return render(request, "store/contacts.html", context)


def message(request):
    if request.method == 'POST':
        send = Contacts()
        send.name = request.POST.get('name')
        send.gmail = request.POST.get('gmail')
        send.number = request.POST.get('number')
        send.message = request.POST.get('message')
        send.save()
        return HttpResponseRedirect('/')


def email_news(request):
    try:
        if request.method == 'POST':
            send = news_email()
            send.email = request.POST.get('search')
            send.save()
            messages.success(request, "Успешно отпрвалено")
            return HttpResponseRedirect('/')
    except:
        messages.success(request, "Ой что то пошло не так")
        return HttpResponseRedirect('/')
