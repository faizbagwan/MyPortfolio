from django.db import models

# Create your models here.
class Student (models.Model):
   #id = models. AutoField()
   name = models.CharField(max_length=100)
   age = models. IntegerField()
   email = models. EmailField()
   address = models. TextField()
   image = models. ImageField()
   file = models. FileField()

class Product(models.Model):
   pass

class Contact(models.Model):
   full_name = models.CharField()
   email = models. EmailField()
   phone = models.CharField(max_length=15)
   email_sub = models.CharField(max_length=200)
   message = models.TextField()