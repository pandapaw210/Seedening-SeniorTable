from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .forms import *
from .models import *



def literature(request):
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

        context = {
            'booksForm': booksForm,
            'books': books,
        }
        return render(request, 'books.html', context)
