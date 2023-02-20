from django.urls import path
from . import views

urlpatterns = [
	path('', views.preventGame, name='preventGame'),
    path('flappybird/', views.flappybird, name='flappybird'),
    path('snake/', views.snake, name='snake'),
    path('guess/', views.guess, name='guess'),
    path('flood/', views.flood, name='flood'),
    path('tetris/', views.tetris, name='tetris'),
    path('word/', views.word, name='word'),
]