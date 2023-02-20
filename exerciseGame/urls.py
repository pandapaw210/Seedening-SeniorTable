from django.urls import path
from . import views

urlpatterns = [
	path('', views.exerciseGame, name='exerciseGame'),
	path('cube3D/', views.cube3D, name='cube3D'),
	path('piano/', views.piano, name='piano'),
]