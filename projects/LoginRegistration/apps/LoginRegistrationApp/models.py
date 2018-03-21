from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {};
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if not postData['first_name'].isalpha:
            errors['first_name_alpha'] = "First name must be letters only"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not postData['last_name'].isalpha:
            errors['last_name_alpha'] = "First name must be letters only"
        if not re.match('[^@]+@[^@]+\.[^@]+',postData['email']):
            errors['email'] = "Emails must be in the Someone@Something.ending format"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters"
        if postData['password'] != postData['conf']:
            errors['unmatched'] = "Passwords do not match"
        return errors
        
    def login_validator(self, postData):
        errors = {};
        if not re.match('[^@]+@[^@]+\.[^@]+',postData['email']):
            errors['email'] = "Emails must be in the Someone@Something.ending format"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must be at least 8 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    birthday = models.DateField(auto_now = False, auto_now_add = False)
    ### HI THIS IS SUPER IMPORTANT IF IT WORKS ###
    objects = UserManager()
    def __repr__(self):
        return self.first_name;