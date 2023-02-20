from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.


def creativeGame(request):
	return render(request, 'creativeGame.html', {})

def pixelart(request):
	return render(request, 'pixelart.html', {})

def drawing(request):
	return render(request, 'drawing.html', {})

def tangram(request):
	return render(request, 'tangram.html', {})

def pianoplay(request):
	return render(request, 'pianoplay.html', {})

