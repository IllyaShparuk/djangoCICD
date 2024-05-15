from django.shortcuts import render
from .models import GameLibItem, UserGamesLib
from cart.models import Cart, CartItem
from cart.views import clear_cart

def add_items_to_lib(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    games = [cart_item.product for cart_item in cart_items]
    user_lib, _ = UserGamesLib.objects.get_or_create(user=request.user)
    
    for item in games:
        lib_item = GameLibItem.objects.create(lib=user_lib, game=item)
        lib_item.generate_game_key()
    
    clear_cart(request)

    user_games_list = GameLibItem.objects.filter(lib=user_lib.id)

    return render(request, 'user_lib.html', context={'user_games_list' : user_games_list})


def open_user_lib(request):
    user_lib, _ = UserGamesLib.objects.get_or_create(user=request.user)
    user_games_list = GameLibItem.objects.filter(lib=user_lib)
    return render(request, 'user_lib.html', context={'user_games_list' : user_games_list})

