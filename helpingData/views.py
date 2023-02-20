from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .forms import *
from .models import *


def helpingData(request):
	return render(request, 'helpingData.html', {})


def books(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']

        books = Books(
            title=title,
            author=author,
            content=content,

        )
        books.save()
        return redirect('books')

    else:
        page = request.GET.get("page")
        booksForm = BooksForm
        books = Books.objects.all()
        paginator = Paginator(books, 10)
        helpingDataBooks = paginator.get_page(page)
        context = {
            'booksForm': booksForm,
            'books': books,
        }
        return render(request, 'books.html', context)


def helpingDataTip1(request):
	return render(request, 'helpingDataTip1.html', {})

def helpingDataTip2(request):
	return render(request, 'helpingDataTip2.html', {})

def helpingDataTip3(request):
	return render(request, 'helpingDataTip3.html', {})

def helpingDataTip4(request):
	return render(request, 'helpingDataTip4.html', {})

def helpingDataTip5(request):
	return render(request, 'helpingDataTip5.html', {})
