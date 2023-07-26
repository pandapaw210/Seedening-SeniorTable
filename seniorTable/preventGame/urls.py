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
    path('ant/', views.ant, name='ant'),
    path('apple/', views.apple, name='apple'),
    path('space/', views.space, name='space'),
    path('pin/', views.pin, name='pin'),
    path('ball/', views.ball, name='ball'),
    path('bejeweled/', views.bejeweled, name='bejeweled'),
    path('stick/', views.stick, name='stick'),
    path('connect/', views.connect, name='connect'),
]