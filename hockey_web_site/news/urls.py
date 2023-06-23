from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('news/club/', club_news, name='club_news'),
    path('news/<int:post_id>', show_post, name='post'),
]
