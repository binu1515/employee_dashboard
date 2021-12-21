from django.db import models


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100,default='python') 
    dept = models.CharField(max_length=100,default='') 

CHECK= [
    ('checked', 'Checkin'),
    ('inside', 'Inside'),
    ('out', 'Checkout'),
    ]

class visitor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=100)
    employee = models.CharField(max_length=100)
    
    #check = (
        #('checked', 'Checkin'),
        #('inside', 'Inside'),
        #('out', 'Checkout'),
    #)
    visitorstatus = models.CharField(max_length=100,choices=CHECK)
        