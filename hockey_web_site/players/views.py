from django.shortcuts import render

from .models import Players, Category


def players(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'title': 'Страница команды'
    }
    return render(request, 'players/players.html', context=context)


def player_info(request, post_id):
    return render(request, 'news/post.html')
