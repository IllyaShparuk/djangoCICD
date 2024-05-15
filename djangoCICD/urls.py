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
from django.urls import path, include

from djangoCICD import settings
from main.views import home
from account.views import sign_up
from cart.views import add_to_cart, open_cart, delete_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('sign-up', sign_up, name='sign_up'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('open_cart', open_cart, name='open_cart'),
    path('delete_from_cart', delete_from_cart, name='delete_from_cart')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)