from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from store.models import Product, Wishlist


@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': wishlist}
    return render(request, 'store/wishlist.html', context)


def addToWishlist(request, id):
    try:
        wishlist = Wishlist()
        product = Product.objects.get(id=id)
        wishlist.product = product
        wishlist.user = request.user
        wishlist.save()
        messages.success(request, "Добавлено в список желаний")
        return redirect('home')
    except:
        messages.success(request, "Ой что то пошло не так")
        return redirect('home')


def deletewishlistitem(request, id):
    try:
        wishlist = Wishlist.objects.get(id=id)
        wishlist.delete()
        messages.success(request, "Удалено успешно")
        return HttpResponseRedirect('/wishlist')
    except:
        messages.success(request, "Ой что то пошло не так")
        return HttpResponseRedirect('/wishlist')