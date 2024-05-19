from django.test import TestCase
from django.urls import reverse
from .models import Game, GameDeveloper

class GameSearchTestCase(TestCase):
    def setUp(self):
        self.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            developer_photo='http://example.com/dev1.jpg',
            ref_to_social='http://example.com'
        )
        self.game1 = Game.objects.create(
            game_name='Game 1',
            slug='game-1',
            price=9.99,
            rating=4.5,
            genre='Action',
            release_date='2023-05-17',
            developer=self.developer,
            game_photo='http://example.com/game1.jpg'
        )
        self.game2 = Game.objects.create(
            game_name='Game 2',
            slug='game-2',
            price=14.99,
            rating=4.0,
            genre='Adventure',
            release_date='2022-12-31',
            developer=self.developer,
            game_photo='http://example.com/game2.jpg'
        )

    def test_game_search_with_query(self):
        response = self.client.get(reverse('game_search'), {'q': 'Game 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Game 1')
        self.assertNotContains(response, 'Game 2')


class SortDateTestCase(TestCase):
    def setUp(self):
        self.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            developer_photo='http://example.com/dev1.jpg',
            ref_to_social='http://example.com'
        )
        self.game1 = Game.objects.create(
            game_name='Game 1',
            slug='game-1',
            price=9.99,
            rating=4.5,
            genre='Action',
            release_date='2023-05-17',
            developer=self.developer,
            game_photo='http://example.com/game1.jpg'
        )
        self.game2 = Game.objects.create(
            game_name='Game 2',
            slug='game-2',
            price=14.99,
            rating=4.0,
            genre='Adventure',
            release_date='2023-05-17',
            developer=self.developer,
            game_photo='http://example.com/game2.jpg'
        )

    def test_sort_date_asc(self):
        response = self.client.get(reverse('sort_date') + '?sort=asc')
        self.assertEqual(response.status_code, 200)
        games = response.context['games']
        self.assertLessEqual(games[0].release_date, games[1].release_date)

    def test_sort_date_desc(self):
        response = self.client.get(reverse('sort_date') + '?sort=desc')
        self.assertEqual(response.status_code, 200)
        games = response.context['games']
        self.assertGreaterEqual(games[0].release_date, games[1].release_date)


class RatingOutputTestCase(TestCase):
    def setUp(self):
        self.developer = GameDeveloper.objects.create(
            developer_name='Test Developer',
            slug='test-developer',
            developer_photo='http://example.com/dev1.jpg',
            ref_to_social='http://example.com'
        )
        self.game1 = Game.objects.create(
            game_name='Game 1',
            slug='game-1',
            price=9.99,
            rating=4.5,
            genre='Action',
            release_date='2023-05-17',
            developer=self.developer,
            game_photo='http://example.com/game1.jpg'
        )
        self.game2 = Game.objects.create(
            game_name='Game 2',
            slug='game-2',
            price=14.99,
            rating=3.2,
            genre='Adventure',
            release_date='2022-12-31',
            developer=self.developer,
            game_photo='http://example.com/game2.jpg'
        )

    def test_rating_output(self):
        self.assertEqual(self.game1.rating_output(), '★★★★☆')
        self.assertEqual(self.game2.rating_output(), '★★★☆☆')