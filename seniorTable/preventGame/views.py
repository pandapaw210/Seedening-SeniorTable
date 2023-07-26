from django.shortcuts import render

# Create your views here.


def preventGame(request):
	return render(request, 'preventGame.html', {})

def flappybird(request):
	return render(request, 'flappybird.html', {})

def snake(request):
	return render(request, 'snake.html', {})

def guess(request):
	return render(request, 'guess.html', {})

def flood(request):
	return render(request, 'flood.html', {})

def tetris(request):
	return render(request, 'tetris.html', {})

def word(request):
	return render(request, 'word.html', {})

def ant(request):
	return render(request, 'ant.html', {})

def apple(request):
	return render(request, 'apple.html', {})

def space(request):
	return render(request, 'space.html', {})

def pin(request):
	return render(request, 'pin.html', {})

def ball(request):
	return render(request, 'ball.html', {})

def bejeweled(request):
	return render(request, 'bejeweled.html', {})

def stick(request):
	return render(request, 'stick.html', {})

def connect(request):
	return render(request, 'connect.html', {})