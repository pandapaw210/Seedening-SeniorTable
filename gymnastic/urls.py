from django.urls import path
from . import views

urlpatterns = [
	path('', views.gymnastic, name='gymnastic'),
	path('gymnastic1/', views.gymnastic1, name='gymnastic1'),
	path('gymnastic2/', views.gymnastic2, name='gymnastic2'),
	path('gymnastic3/', views.gymnastic3, name='gymnastic3'),
	path('gymnastic4/', views.gymnastic4, name='gymnastic4'),
	path('gymnastic5/', views.gymnastic5, name='gymnastic5'),
	path('gymnastic6/', views.gymnastic6, name='gymnastic6'),
	path('gymnastic7/', views.gymnastic7, name='gymnastic7'),
	path('gymnastic8/', views.gymnastic8, name='gymnastic8'),
	path('gymnastic9/', views.gymnastic9, name='gymnastic9'),
	path('gymnastic10/', views.gymnastic10, name='gymnastic10'),
	path('gymnastic11/', views.gymnastic11, name='gymnastic11'),
	path('gymnastic12/', views.gymnastic12, name='gymnastic12'),
	path('gymnastic13/', views.gymnastic13, name='gymnastic13'),
]