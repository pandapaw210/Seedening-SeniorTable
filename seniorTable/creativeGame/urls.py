from django.urls import path
from . import views

urlpatterns = [
	path('', views.creativeGame, name='creativeGame'),
	path('pixelart/', views.pixelart, name='pixelart'),
	path('drawing/', views.drawing, name='drawing'),
    path('tangram/', views.tangram, name='tangram'),
    path('pianoplay/', views.pianoplay, name='pianoplay'),
]