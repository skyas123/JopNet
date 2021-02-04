from django.db import models

# Create your models here.

class Persons(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    date_of_appearence=models.DateField(auto_now=False, auto_now_add=False)
    size=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='Static/pictures/ava/', height_field=None, width_field=None, max_length=100)

    def _str_(self):
        return self.first_name
    def _str_(self):
        return self.second_name
    def _str_(self):
        return self.date_of_appearence
    def _str_(self):
        return self.size
    def _str_(self):
        return self.photo
     