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

class Department(models.Model):
    name=models.CharField(max_length=100)
class DepartmentRoles(models.Model):
    departmentId=models.ForeignKey(Department,on_delete=models.CASCADE)
    admin=models.CharField(max_length=100)    
    user=models.CharField(max_length=100)    
    manager=models.CharField(max_length=100)

class Ticket(models.Model):
    ticketNumber=models.CharField(primary_key=True,max_length=100)
    issue_department=models.CharField(max_length=100)
    issue=models.TextField() 
    issue_creation_date=models.TextField(max_length=100)
    is_this_new_ticket=models.CharField(max_length=100)

