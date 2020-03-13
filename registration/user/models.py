from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    def __unicode__(self):
        return self.username
    # def __init__(self,username,email,password):
    #     self.username=username
    #     self.password=password
    #     self.email=email
class Post(models.Model):
    postname=models.CharField(max_length=100)    