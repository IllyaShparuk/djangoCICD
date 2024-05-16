from django.shortcuts import render
from .models import Game


def home(request):
    games = Game.objects.all()

    return render(request, 'main.html', context={
        'games': games
    })

def game_list(request):
    sort_order = request.GET.get('sort')
    if sort_order == 'desc':
        games = Game.objects.all().order_by('-release_date')
    else:
        games = Game.objects.all().order_by('release_date')
    return render(request, 'main.html', {'games': games, 'sort_order': sort_order})