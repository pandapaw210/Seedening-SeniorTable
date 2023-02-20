from django.urls import path
from . import views

urlpatterns = [
	path('', views.preventGame, name='preventGame'),
    path('sudoku/', views.sudoku, name='sudoku'),
    path('flappybird/', views.flappybird, name='flappybird'),
]