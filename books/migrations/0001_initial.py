# Generated by Django 2.2.6 on 2019-10-05 04:54

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_desc', models.TextField()),
                ('book_title', models.CharField(max_length=200)),
                ('book_edition', models.CharField(max_length=200)),
                ('book_rating', models.FloatField()),
                ('book_isbn', models.BigIntegerField()),
                ('book_pages', models.IntegerField()),
                ('book_rating_count', models.IntegerField()),
                ('book_review_count', models.IntegerField()),
                ('book_authors', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=20, size=None)),
                ('genres', django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=20, size=None)),
                ('image_url', models.URLField()),
                ('checked_out', models.BooleanField()),
            ],
        ),
    ]