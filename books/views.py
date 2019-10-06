# Django configs
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# models
from .models import Book

# etc
from tablib import Dataset


# Create your views here.

# /books
def index(request):
  books = Book.objects.all()

  template = loader.get_template('books/index.html')

  context = {
    'books': books,
  }

  return HttpResponse(template.render(context, request))

# /books/1
def detail(request, book_id):
  book = Book.objects.get(book_id)

  template = loader.get_template('books/detail.html')

  context = {
    'book': book
  }

  return HttpResponse(template.render(context, request))
