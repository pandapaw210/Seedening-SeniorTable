from django.shortcuts import render

# Create your views here.



def logicGame(request):
	return render(request, 'logicGame.html', {})

def memoryGame(request):
	return render(request, 'memoryGame.html', {})

def puzzle(request):
	return render(request, 'puzzle.html', {})

def game2048(request):
	return render(request, '2048.html', {})

def hanoitower(request):
	return render(request, 'hanoitower.html', {})

def Omok(request):
	return render(request, 'Omok.html', {})

def binairo(request):
	return render(request, 'binairo.html', {})

def sudoku(request):
	return render(request, 'sudoku.html', {})

def square(request):
	return render(request, 'square.html', {})




