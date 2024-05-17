from django.db import models
from django.contrib.auth.models import User
from main.models import Game
from decimal import Decimal
from django.db.models import Sum


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    is_paid = models.BooleanField(default=False)
    cart_price = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal('0.00'))

    def calculate_cart_price(self):
        total_price = self.cart_items.aggregate(total=Sum('product__price'))['total'] or Decimal('0')
        self.cart_price = total_price
        self.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)