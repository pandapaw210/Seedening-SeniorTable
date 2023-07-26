from django.shortcuts import render

# Create your views here.




def worldAlbum(request):
	return render(request, 'worldAlbum.html', {})