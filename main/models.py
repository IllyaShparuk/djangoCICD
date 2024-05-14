from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class GameDeveloper(models.Model):
    developer_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    developer_photo = models.ImageField(upload_to='dev_photo/', blank=True, null=True)
    ref_to_social = models.CharField(max_length=255)


    def __str__(self):
        return self.developer_name


class Game(models.Model):
    game_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    rating = models.DecimalField(validators=[MaxValueValidator(5), MinValueValidator(0)], max_digits=20, decimal_places=2)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    developer = models.ForeignKey(GameDeveloper, on_delete= models.CASCADE, related_name='games')
    game_photo = models.ImageField(upload_to='games_photo/', blank=True, null=True)
    
        


    