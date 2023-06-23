from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import News, Category


def index(request):
    posts = News.objects.all()[:4]
    context = {
        'posts': posts,
        'title': 'Главная страница'
    }
    return render(request, 'news/index.html', context=context)


def news(request):
    all_posts = News.objects.all()
    paginator = Paginator(all_posts, 8)  # Разбиваем посты на страницы, по 5 постов на каждой странице
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект текущей страницы

    context = {'page_obj': page_obj, }

    return render(request, 'news/news.html', context=context)


def club_news(request, category_slug='klub'):
    # Получаем объект категории по slug
    category = Category.objects.get(slug=category_slug)

    # Получаем все новости с указанной категорией
    all_posts = News.objects.filter(cat=category, is_published=True)
    paginator = Paginator(all_posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, }

    return render(request, 'news/club_news.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(News, id=post_id)
    return render(request, 'news/post.html', {'post': post, })
