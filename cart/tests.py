from django.test import TestCase, Client
from django.contrib.auth.models import User
from main.models import Game, GameDeveloper
from decimal import Decimal
from .models import Cart, CartItem

class CartTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            ref_to_social='http://example.com'
        )
        self.game1 = Game.objects.create(
            game_name='Game 1',
            slug='game-1',
            price=Decimal('9.99'),
            rating=4.5,
            genre='Action',
            release_date='2023-05-17',
            developer=self.developer,
            game_photo='http://example.com/game1.jpg'
        )
        self.game2 = Game.objects.create(
            game_name='Game 2',
            slug='game-2',
            price=Decimal('14.99'),
            rating=4.0,
            genre='Adventure',
            release_date='2022-12-31',
            developer=self.developer,
            game_photo='http://example.com/game2.jpg'
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item1 = CartItem.objects.create(cart=self.cart, product=self.game1)
        self.cart_item2 = CartItem.objects.create(cart=self.cart, product=self.game2)

    def test_cart_creation(self):
        self.assertEqual(self.user.cart.count(), 1)
        self.assertEqual(self.user.cart.first(), self.cart)
        self.assertFalse(self.cart.is_paid)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart.cart_items.count(), 2)
        self.assertIn(self.cart_item1, self.cart.cart_items.all())
        self.assertIn(self.cart_item2, self.cart.cart_items.all())

    def test_calculate_cart_price(self):
        self.cart.calculate_cart_price()
        expected_total = self.game1.price + self.game2.price
        self.assertAlmostEqual(self.cart.cart_price, expected_total, places=2)
