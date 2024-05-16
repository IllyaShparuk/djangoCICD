from django.shortcuts import render
from .models import Game


def home(request):
    games = Game.objects.all()

    return render(request, 'main.html', context={
        'games': games
    })

#Сортування за датою релізу
def sort_date(request):
    sort_order = request.GET.get('sort')
    if sort_order == 'desc':
        games = Game.objects.all().order_by('-release_date')
    else:
        games = Game.objects.all().order_by('release_date')
    return render(request, 'main.html', {'games': games, 'sort_order': sort_order})

#Сортування за рейтингом
def sort_rating(request):
    sort_order = request.GET.get('sort')
    if sort_order == 'desc':
        games = Game.objects.all().order_by('-rating')
    else:
        games = Game.objects.all().order_by('rating')
    return render(request, 'main.html', {'games': games, 'sort_order': sort_order})

#Сортування за ціною
def sort_price(request):
    sort_order = request.GET.get('sort')
    if sort_order == 'desc':
        games = Game.objects.all().order_by('-price')
    else:
        games = Game.objects.all().order_by('price')
    return render(request, 'main.html', {'games': games, 'sort_order': sort_order})

def game_search(request):
    query = request.GET.get('q')  # Отримуємо параметр пошуку з URL
    if query:
        games = Game.objects.filter(game_name__icontains=query)  # Фільтруємо ігри за частковим входженням імені
    else:
        games = Game.objects.all()  # Якщо пошуковий запит порожній, повертаємо усі ігри
    return render(request, 'main.html', {'games': games, 'query': query})

