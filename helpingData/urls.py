from django.urls import path
from . import views

urlpatterns = [
	path('', views.helpingData, name='helpingData'),
    path('books/', views.books, name='books'),
	path('helpingDataTip1/', views.helpingDataTip1, name='helpingDataTip1'),
	path('helpingDataTip2/', views.helpingDataTip2, name='helpingDataTip2'),
	path('helpingDataTip3/', views.helpingDataTip3, name='helpingDataTip3'),
	path('helpingDataTip4/', views.helpingDataTip4, name='helpingDataTip4'),
	path('helpingDataTip5/', views.helpingDataTip5, name='helpingDataTip5'),
	path('helpingDataTip6/', views.helpingDataTip6, name='helpingDataTip6'),
]