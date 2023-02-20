from django.urls import path
from . import views

urlpatterns = [
	path('', views.diagnosis, name='diagnosis'),
	path('diagnosisResult/', views.diagnosisResult, name='diagnosisResult'),
]