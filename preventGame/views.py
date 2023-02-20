from django.shortcuts import render

# Create your views here.



def preventGame(request):
	return render(request, 'preventGame.html', {})

def sudoku(request):
	return render(request, 'sudoku.html', {})

def flappybird(request):
	return render(request, 'flappybird.html', {})