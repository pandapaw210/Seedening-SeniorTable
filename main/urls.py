from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('logicGame/', include('logicGame.urls'), name="logicGame"),
	path('creativeGame/', include('creativeGame.urls'), name="creativeGame"),
	path('exerciseGame/', include('exerciseGame.urls'), name="exerciseGame"),
	path('preventGame/', include('preventGame.urls'), name="preventGame"),
	path('gymnastic/', include('gymnastic.urls'), name="gymnastic"),
	path('helpingData/', include('helpingData.urls'), name="helpingData"),
	path('literature/', include('literature.urls'), name="literature"),
	path('diagnosis/', include('diagnosis.urls'), name="diagnosis"),
	path('loveMessage/', include('loveMessage.urls'), name="loveMessage"),
	path('worldAlbum/', include('worldAlbum.urls'), name="worldAlbum"),
]