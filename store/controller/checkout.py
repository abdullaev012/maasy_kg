import random
import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from store.models import *
from store.forms import send_report


@login_required(login_url='loginpage')
def index(request):
    size_pro = Size.objects.all()
    q = False
    for i in size_pro:
        if i.quantity <= 20:
            q = True

    cart = Cart.objects.all()
    total_price = 0
    qg = False
    if cart.exists():
        qg = True
    for i in cart:
        total_price += i.product.selling_price * i.quantity

    context = {'cart': cart, 'qg': qg, 'total_price': total_price, 'q': q, 'size_pro': size_pro}
    return render(request, "store/checkout.html", context)

# @login_required(login_url='loginpage')
# def refresh(request):
#     print('etrytdfughyjklproduct_nameproduct_nameproduct_name')
#     products_in_cart = Order_product.objects.all()
#     total_price = 0
#     for i in products_in_cart:
#         juan = request.get(f'selected_size_{i.product_name}')
#         i.quantity = juan
#         i.save()
#         total_price += i.product_name.selling_price * i.quantity

#     context = {'products_in_cart':products_in_cart, 'total_price':total_price}
#     return render(request, "store/checkout.html", context)


@login_required(login_url='loginpage')
def placeorder(request):
    try:
        if request.method == 'POST':
            currentuser = User.objects.filter(id=request.user.id).first()
            if not currentuser.first_name:
                currentuser.first_name = request.POST.get('fname')
                currentuser.last_name = request.POST.get('lname')
                currentuser.save()
            if not Profile.objects.filter(user=request.user):
                userprofile = Profile()
                userprofile.user = request.user
                userprofile.phone = request.POST.get('phone')
                userprofile.address = request.POST.get('address')
                userprofile.city = request.POST.get('city')
                userprofile.state = request.POST.get('state')
                userprofile.country = request.POST.get('country')
                userprofile.save()
            neworder = Order()
            neworder.user = request.user
            neworder.fname = request.POST.get('fname')
            neworder.lname = request.POST.get('lname')
            neworder.email = request.POST.get('email')
            neworder.phone = request.POST.get('phone')
            neworder.address = request.POST.get('address')
            neworder.city = request.POST.get('city')
            neworder.state = request.POST.get('state')
            neworder.country = request.POST.get('country')
            neworder.payment_method = request.POST.get('payment_method')
            neworder.total_price = request.POST.get('total_price')
            trackno = str(random.randint(11111111, 99999999))
            while Order.objects.filter(tracking_no=trackno) is None:
                trackno = str(random.randint(11111111, 99999999))
            neworder.tracking_no = trackno
            neworder.save()
            cart = Cart.objects.filter(user=request.user)
            for item in cart:
                i = OrderItem()
                i.order = neworder
                i.product = item.product
                i.price = item.product.selling_price
                i.quantity = item.quantity
                i.size = item.size
                i.save()

                size = Size.objects.get(product=item.product, size=item.size)
                size.quantity -= item.quantity
                size.save()
            r = Cart.objects.filter(user=request.user)
            for b in r:
                b.delete()
            send_report()
        messages.success(request, "Ваш заказ успешно подвержден")
        return HttpResponseRedirect('/')
    except:
        r = Cart.objects.filter(user=request.user)
        for b in r:
            b.delete()
        size = Size.objects.all()
        for i in size:
            if i.quantity == 0:
                messages.success(request, "У нас на складе не осталось такой товар")
                return render(request, "store/cart.html")
