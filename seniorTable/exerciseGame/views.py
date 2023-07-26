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

def pong(request):
	return render(request, 'pong.html', {})

def shooting(request):
	return render(request, 'shooting.html', {})

def jump(request):
	return render(request, 'jump.html', {})

def memorize(request):
	return render(request, 'memorize.html', {})

def car(request):
	return render(request, 'car.html', {})

