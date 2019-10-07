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
  # https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
  books = Book.objects.all()

  order_by = request.GET.get('order_by')

  if order_by:
    # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/asc_or_desc.html
    books = Book.objects.all().order_by(order_by)

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

    # force client back to books index action
    return redirect('/books')

# I was going to use 'return' for this action
# however it seems it's a reserved word in python
# which makes sense :P
def checkin(request, book_id):
  if request.POST:
    book = Book.objects.get(id=book_id)

    # https://docs.djangoproject.com/en/2.2/topics/db/queries/#saving-changes-to-objects
    book.checked_out = False
    book.save()

    # force client back to books index action
    return redirect('/books')