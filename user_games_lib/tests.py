import string

from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Game, GameDeveloper
from .models import UserGamesLib, GameLibItem

class UserGamesLibTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            ref_to_social='http://example.com'
        )
        self.game = Game.objects.create(
            game_name='Test Game',
            slug='test-game',
            price=19.99,
            rating=4.8,
            genre='Action',
            release_date='2023-01-01',
            developer=self.developer,
            game_photo='http://example.com/testgame.jpg'
        )
        self.user_game_lib = UserGamesLib.objects.create(user=self.user)
        self.game_lib_item = GameLibItem.objects.create(lib=self.user_game_lib, game=self.game)

    def test_create_user_game_lib(self):
        self.assertEqual(self.user.games_lib.count(), 1)
        self.assertEqual(self.user.games_lib.first(), self.user_game_lib)

    def test_create_game_lib_item(self):
        self.assertEqual(self.user_game_lib.game_lib_item.count(), 1)
        self.assertEqual(self.user_game_lib.game_lib_item.first(), self.game_lib_item)
        self.assertEqual(self.game_lib_item.game, self.game)

    def test_generate_game_key(self):
        self.assertIsNone(self.game_lib_item.game_key)
        self.game_lib_item.generate_game_key()
        self.assertIsNotNone(self.game_lib_item.game_key)
        self.assertEqual(len(self.game_lib_item.game_key), 10)
        self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in self.game_lib_item.game_key))
