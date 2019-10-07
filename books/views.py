# Django configs
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# https://realpython.com/django-redirects/#django-redirects-a-super-simple-example
from django.shortcuts import redirect

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
  book = Book.objects.get(id=book_id)

  template = loader.get_template('books/detail.html')

  context = {
    'book': book
  }

  return HttpResponse(template.render(context, request))

def checkout(request, book_id):
  if request.POST:
    book = Book.objects.get(id=book_id)

    # https://docs.djangoproject.com/en/2.2/topics/db/queries/#saving-changes-to-objects
    book.checked_out = True
    book.save()

    return redirect('/books')

# I was going to use 'return' for this action
# however it seems its a reserved word in python
# which makes sense
def checkin(request, book_id):
  if request.POST:
    book = Book.objects.get(id=book_id)

    # https://docs.djangoproject.com/en/2.2/topics/db/queries/#saving-changes-to-objects
    book.checked_out = False
    book.save()

    return redirect('/books')