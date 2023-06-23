from django.urls import path
from .views import *


urlpatterns = [
    path('', players, name='players'),
    path('<int:player_id>', player_info, name='player_info'),
]
