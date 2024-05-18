"""
URL configuration for djangoCICD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from djangoCICD import settings
from main.views import home
from account.views import sign_up, user_logout
from cart.views import add_to_cart, open_cart, delete_from_cart
from user_games_lib.views import add_items_to_lib, open_user_lib
from main.views import sort_date, sort_rating, sort_price, game_search



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('sign-up', sign_up, name='sign_up'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('open_cart', open_cart, name='open_cart'),
    path('delete_from_cart', delete_from_cart, name='delete_from_cart'),
    path('add_items_to_lib', add_items_to_lib, name='add_items_to_lib'),
    path('open_user_lib', open_user_lib, name='open_user_lib'),
    path('user_logout', user_logout, name='user_logout'),
    path('sort_date', sort_date, name='sort_date'),
    path('sort_rating', sort_rating, name='sort_rating'),
    path('sort_price', sort_price, name='sort_price'),
    path('game_search', game_search, name='game_search'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]