from __future__ import unicode_literals
from django.db import models

# Create your models here.
# One class for each table
#unique id is created automatically
class Blog(models.Model):
    name = models.CharField(max_length=255);
    desc = models.TextField();
    created_at = models.DateTimeField(auto_now_add = True);
    updated_at = models.DateTimeField(auto_now = True);
    def __repr__(self):
        return "<Blog object: {}: {}>".format(self.name, self.desc)
class Comment(models.Model):
    comment = models.CharField(max_length=140);
    created_at = models.DateTimeField(auto_now_add = True);
    updated_at = models.DateTimeField(auto_now = True);
    #one to many, because there can be many comments on one blog
    blog = models.ForeignKey(Blog, related_name = "comments") #blog is singular and comments plural here, because of the one blog, many comments
class Admin(models.Model):
    first_name = models.CharField(max_length=255);
    last_name = models.CharField(max_length=255);
    email = models.CharField(max_length=255);
    blogs = models.ManyToManyField(Blog, related_name = "admins"); #here, both blogs and admins are plural because of the many to many releationshipo
    created_at = models.DateTimeField(auto_now_add = True);
    updated_at = models.DateTimeField(auto_now = True);