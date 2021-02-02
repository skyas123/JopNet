from django.db import models

# Create your models here.

class Persons(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    date_of_appearence=models.DateField(auto_now=False, auto_now_add=False)
    

