from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.board, name='loveMessage'),
	path('view/', views.board2, name='loveMessage2'),
]