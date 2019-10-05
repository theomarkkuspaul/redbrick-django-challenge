from django.db import models

# https://django-mysql.readthedocs.io/en/latest/model_fields/list_fields.html#list-fields
from django_mysql.models import ListCharField

# Create your models here.

class Book(models.Model):
    book_desc = models.TextField() # 'A large text field'
    book_title = models.CharField(max_length=200) # small-to-large size strings. Given book titles need to read across a hand-held sized object, we should not need to support large text fields.
    book_edition = models.CharField(max_length=200, null=True) # a concise statement
    book_rating = models.FloatField(null=True) # floating point value with two-decimal points max.
    book_isbn = models.BigIntegerField(null=True) # ISBN are 13 numerical digits long, therefore have decided to use a 64 bit integer
    book_pages = models.IntegerField(null=True) # a value ranging from tens to hundreds. Well within memory bounds of IntegerField
    book_rating_count = models.IntegerField(null=True) # numerical value
    book_review_count = models.IntegerField(null=True) # numerical value
    book_authors = ListCharField(base_field=models.CharField( max_length=100), max_length=20) # store a collection of strings -- author name(s)
    genres = ListCharField(base_field=models.CharField(max_length=100), max_length=20) # store a collection of strings -- 'action', 'adventure', 'romance', 'django for dummies'
    image_url = models.URLField(null=True) # like CharField but with better support for url strings
    checked_out = models.BooleanField(default=False) # a book is either in the library or someone has checked it out
