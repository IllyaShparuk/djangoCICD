from django.shortcuts import render, redirect
from main.models import Game
from django.http import Http404
from .models import Cart, CartItem


def add_to_cart(request):
    if request.user.id is None:
        return redirect('login/')
    product_id = request.GET.get('product_id')
    try:
        product = Game.objects.get(pk=product_id)
    except Game.DoesNotExist:
        raise Http404("Product does not exist")
    
    user_cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False, defaults={'cart_price': 0})
    CartItem.objects.create(cart=user_cart, product=product)
    user_cart.calculate_cart_price()
    cart_items = CartItem.objects.filter(cart=user_cart)
    return render(request, 'user_orders.html', context={'cart_items' : cart_items})


def delete_from_cart(request):
    cart_item_id = request.GET.get('cart_item_id')
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    user_cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False, defaults={'cart_price': 0})

    cart_items = CartItem.objects.filter(cart=user_cart)

    return render(request, 'user_orders.html', context={'cart_items': cart_items})


def clear_cart(request):
    user_cart = Cart.objects.get(user=request.user, is_paid=False)
    user_cart.delete()


def open_cart(request):
    if request.user.id is None:
        return redirect('login/')
    user_cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False, defaults={'cart_price': 0})
    cart_items = CartItem.objects.filter(cart=user_cart)
    return render(request, 'user_orders.html', context={'cart_items' : cart_items})


