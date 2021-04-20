from django.db import models

# Create your models here.

class Persons(models.Model):
     first_name=models.CharField(max_length=30,default='')
     second_name=models.CharField(max_length=30,default='')
     date_of_appearence=models.DateField(auto_now=False, auto_now_add=False)
     size=models.IntegerField(null=True,blank=True,default=0)
     ava=models.ForeignKey("Media",on_delete=models.CASCADE,blank=True,null=True)
     login=models.CharField(max_length=30,default='')
     password=models.CharField(max_length=30,default='')
     friends = models.ManyToManyField("self",blank=True,null=True)

    # за что отвечает функция ниже?

     def _str_(self):
        return self.first_name
     def _str_(self):
        return self.second_name
     def _str_(self):
        return self.date_of_appearence
     def _str_(self):
        return self.size
     def _str_(self):
        return self.ava
    


class Media(models.Model):
    photo=models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100,null=True,blank=True)

class Posts(models.Model):
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    subphoto=models.ManyToManyField("Media")
    author=models.ForeignKey(Persons,on_delete=models.CASCADE,null=True)
    like=models.IntegerField(null=True,blank=True,default=0)


class Dialogs(models.Model):
 listOfMembers=models.ManyToManyField("Persons")
 dialogPfoto=models.ForeignKey(Media,on_delete=models.CASCADE,null=True)
 date_of_appearence=models.DateTimeField(auto_now_add=True)
 dialogname=models.CharField(max_length=30,default='')

class Message(models.Model):
 date_of_appearence=models.DateTimeField(auto_now_add=True)
 text=models.TextField()
 atachment=models.ForeignKey(Dialogs,on_delete=models.CASCADE,null=True)
 subphoto=models.ManyToManyField("Media")
 author=models.ForeignKey(Persons,on_delete=models.CASCADE,null=True)
 