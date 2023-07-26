from django.forms import ModelForm

from .models import *


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'content']

