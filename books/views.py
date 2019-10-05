# Django configs
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# models
from .models import Book

# etc
from tablib import Dataset


# Create your views here.

def index(request):
  books = Book.objects.all()

  template = loader.get_template('books/index.html')

  context = {
    'books': books,
  }

  return HttpResponse(template.render(context, request))

def upload(request):
  if request.method == 'POST':
    book_resource = BookResource()
    dataset = Dataset()
    csv_file = request.FILES['myfile']

    imported_data = dataset.load(csv_file.read())
    result = book_resource.import_data(dataset, dry_run=True)  # Test the data import

    if not result.has_errors():
      book_resource.import_data(dataset, dry_run=False)  # Actually import now

  return render(request, 'books/upload.html')