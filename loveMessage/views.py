from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .forms import *
from .models import *

def board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']


        board = Board(
            title=title,
            content=content,

        )
        board.save()
        return redirect('loveMessage')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board.html', context)


def board2(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        board = Board(
            title=title,
            content=content,

        )
        board.save()
        return redirect('loveMessage2')

    else:
        page = request.GET.get("page")
        boardForm = BoardForm
        board = Board.objects.order_by('?')
        paginator = Paginator(board, 10)
        loveMessage = paginator.get_page(page)
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'board2.html', context)
    

   




