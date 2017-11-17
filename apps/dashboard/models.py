from __future__ import unicode_literals
from django.db import models




class Author(models.Model):
    full_name = models.CharField(max_length=255)    
    created_at = models.CharField(auto_now_add = True)
    updated_at = models.CharField(auto_now_add = True)

class Book(models.Model):
    title = models.CharField(max_length=255)    
    created_at = models.CharField(auto_now_add = True)
    updated_at = models.CharField(auto_now_add = True)
    author = models.ForeignKey(Author, related_name='books')
    uploader = models.ForeignKey(Author, related_name='books')
class Review(models.Model):
    comment = models.CharField(max_length=255)    
    rating = models.CharField(auto_now_add = True)
    created_at = models.CharField(auto_now_add = True)
    updated_at = models.CharField(auto_now_add = True)
    reviewer = models.ForeignKey(Author, related_name='user_review')
    book_reviewed = models.ForeignKey(Author, related_name='books')
    