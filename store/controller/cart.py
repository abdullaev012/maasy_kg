from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from store.models import *


def addtocart(request, id):
    try:
        cart = Cart()
        product = Size.objects.get(id=id)
        cart.product = product.product
        cart.user = request.user
        cart.size = product.size
        cart.save()
        messages.success(request, "Добавлено в корзину")
        return redirect('home')
    except:
        messages.success(request, "Ой что то пошло не так")
        return redirect('home')


@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, "store/cart.html", context)

def plus(request, id):
    cart = Cart.objects.get(id=id)
    size = Size.objects.get(product=cart.product, size=cart.size)
    all_carts = Cart.objects.filter(user=request.user)
    context = {'cart': all_carts}
    if size.quantity-1 >= cart.quantity:
        quantity = cart.quantity + 1
        cart.quantity = quantity
        cart.save()
        return render(request, "store/cart.html", context)
    else:
        messages.success(request, f"У нас на складе осталось {size.quantity} штуков")
        cart = Cart.objects.filter(user=request.user)
        context = {'cart': cart}
        return render(request, "store/cart.html", context)
    
def minus(request, id):
    cart = Cart.objects.get(id=id)
    all_carts = Cart.objects.filter(user=request.user)
    context = {'cart': all_carts}
    if cart.quantity >= 2:
        quantity = cart.quantity - 1
        cart.quantity = quantity
        cart.save()
        return render(request, "store/cart.html", context)
    else:
        messages.success(request, "Минимальная колличество 1")
        cart = Cart.objects.filter(user=request.user)
        context = {'cart': cart}
        return render(request, "store/cart.html", context)



def sendOrder(request):
    return render(request, "store/checkout.html")


def removeCart(request, id):
    try:
        cart = Cart.objects.get(id=id)
        cart.delete()
        messages.success(request, "Удалено успешно")
        return HttpResponseRedirect('/cart')
    except:
        messages.success(request, "Ой что то пошло не так")
        return HttpResponseRedirect('/cart')