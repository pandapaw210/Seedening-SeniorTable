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