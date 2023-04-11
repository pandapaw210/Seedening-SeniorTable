from django.urls import path
from . import views

urlpatterns = [
	path('', views.logicGame, name='logicGame'),
	path('memoryGame/', views.memoryGame, name='memoryGame'),
	path('puzzle/', views.puzzle, name='puzzle'),
	path('2048/', views.game2048, name='2048'),
	path('hanoi/', views.hanoi, name='hanoi'),
	path('Omok/', views.Omok, name='Omok'),
	path('binairo/', views.binairo, name='binairo'),
    	path('sudoku/', views.sudoku, name='sudoku'),
    	path('square/', views.square, name='square'),
	path('freecell/', views.freecell, name='freecell'),
	path('dots/', views.dots, name='dots'),
]
