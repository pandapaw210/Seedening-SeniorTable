from django.shortcuts import render

# Create your views here.



def exerciseGame(request):
	return render(request, 'exerciseGame.html', {})

def cube3D(request):
	return render(request, 'cube3D.html', {})

def piano(request):
	return render(request, 'piano.html', {})

def block(request):
	return render(request, 'block.html', {})

def ball_breaker(request):
	return render(request, 'ball_breaker.html', {})

