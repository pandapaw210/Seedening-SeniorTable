from django.urls import path
from . import views

urlpatterns = [
	path('', views.logicGame, name='logicGame'),
	path('memoryGame/', views.memoryGame, name='memoryGame'),
	path('puzzle/', views.puzzle, name='puzzle'),
	path('2048/', views.game2048, name='2048'),
	path('hanoitower/', views.hanoitower, name='hanoitower'),
	path('Omok/', views.Omok, name='Omok'),
]