from django.test import TestCase
from django.urls import reverse
from .models import Game, GameDeveloper

class GameSearchTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            ref_to_social='http://example.com'
        )
        cls.game1 = Game.objects.create(
            game_name='Game 1',
            slug='game-1',
            price=9.99,
            rating=4.5,
            genre='Action',
            release_date='2023-05-17',
            developer=cls.developer,
            game_photo='http://example.com/game1.jpg'
        )
        cls.game2 = Game.objects.create(
            game_name='Game 2',
            slug='game-2',
            price=14.99,
            rating=4.0,
            genre='Adventure',
            release_date='2022-12-31',
            developer=cls.developer,
            game_photo='http://example.com/game2.jpg'
        )

    # Перевіряємо, як працює функція пошуку ігор, коли у нас є пошуковий запит
    def test_game_search_with_query(self):
        response = self.client.get(reverse('game_search'), {'q': 'Game 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Game 1')
        self.assertNotContains(response, 'Game 2')



