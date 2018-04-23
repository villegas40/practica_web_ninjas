from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from equipos.models import Product


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.add(product, price=product.precio)
    return HttpResponse("Added")


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    return HttpResponse("Removed")


def show(request):
    return render(request, 'equipos/mostrar-carrito.html')
