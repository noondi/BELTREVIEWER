from __future__ import unicode_literals
from django.db import models
import bcrypt
import re


# # Create your models here.
class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True,'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

    def creator(self, postData):
        user = self.create(
        first_name = postData['first_name'],
        last_name = postData['last_name'],
        email = postData['email'],
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()),
        )
        return user 
    def validate(self, postData): 
        print postData
        results = {'status': True,'errors': []}
        #first name validations
        if len(postData['first_name']) < 3:
            results['errors'].append('poor grammar!!')
            results['status'] = False
        #last name validations
        if len(postData['last_name']) < 3:
            results['errors'].append('poor grammar!!')
            results['status'] = False
        # email validations        
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('email invalid!!')
            results['status'] = False
        if postData['password'] != postData['confpw']:
            results['errors'].append('Passwords do not match!!')
            results['status'] = False

        if len(postData['password']) < 8:
            results['errors'].append('Passwords should be at least 8 characters!')
            results['status'] = False

        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('The user already exists')  
            results['status'] = False
        return results     

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    objects = UserManager()



