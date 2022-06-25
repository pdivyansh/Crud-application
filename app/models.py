from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Contact=models.BigIntegerField()
