from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    regno=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    committee=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    nativeplace=models.CharField(max_length=100)
    date= models.DateField()
   