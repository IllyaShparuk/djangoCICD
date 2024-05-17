from django.db import models
from django.contrib.auth.models import User
from main.models import Game
import random
import string



class UserGamesLib(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_lib")
        

class GameLibItem(models.Model):
    lib = models.ForeignKey(UserGamesLib, on_delete=models.CASCADE, related_name="game_lib_item")
    game =  models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
    game_key = models.CharField(max_length=10, null=True)


    def generate_game_key(self):
        characters = string.ascii_uppercase + string.digits
        self.game_key = ''.join(random.choice(characters) for _ in range(10))
        self.save()
