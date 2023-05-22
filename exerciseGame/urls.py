from django.urls import path
from . import views

urlpatterns = [
	path('', views.exerciseGame, name='exerciseGame'),
	path('cube3D/', views.cube3D, name='cube3D'),
	path('piano/', views.piano, name='piano'),
	path('block/', views.block, name='block'),
	path('ball_breaker/', views.ball_breaker, name='ball_breaker'),
	path('pong/', views.pong, name='pong'),
	path('shooting/', views.shooting, name='shooting'),
	path('jump/', views.jump, name='jump'),
	path('memorize/', views.memorize, name='memorize'),
	path('car/', views.car, name='car'),
]