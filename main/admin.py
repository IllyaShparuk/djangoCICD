from django.contrib import admin
from .models import Game, GameDeveloper
from rangefilter.filters import (
    DateRangeFilterBuilder,
    NumericRangeFilterBuilder
)


@admin.register(GameDeveloper)
class GameDeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'developer_name', 'developer_photo', 'ref_to_social')
    list_editable = ('developer_name', 'developer_photo', 'ref_to_social')
    


@admin.register(Game)    
class GameAdmin(admin.ModelAdmin):
    list_filter = (('price', NumericRangeFilterBuilder()),
                   ('rating', NumericRangeFilterBuilder()),
                   'genre',
                   ('release_date', DateRangeFilterBuilder()))
    list_display = ('id', 'game_name', 'price', 'rating', 'genre', 'release_date', 'developer', 'game_photo')
    list_editable = ('game_name', 'price', 'rating', 'genre', 'release_date', 'developer', 'game_photo')

