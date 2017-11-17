# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..beltbelt.models import User



# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)


class Book(models.Model):
    title = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author, related_name="books")
    uploader = models.ForeignKey(User, related_name="uploaded_book")

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    reviewer = models.ForeignKey(User, related_name="user_review")
    book_reviewed = models.ForeignKey(Book, related_name="review_of_book")