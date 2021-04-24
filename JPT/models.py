from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Persons(models.Model):
     user=models.OneToOneField(User, on_delete=models.CASCADE)
     date_of_appearence=models.DateField(auto_now=False, auto_now_add=False,null=True)
     size=models.IntegerField(null=True,blank=True,default=0)
     ava=models.ForeignKey("Media",on_delete=models.CASCADE,blank=True,null=True)
     friends = models.ManyToManyField("self",blank=True,null=True)

     @receiver(post_save, sender=User)
     def create_user_profile(sender, instance, created, **kwargs):
      if created:
        Persons.objects.create(user=instance)

     @receiver(post_save, sender=User)
     def save_user_profile(sender, instance, **kwargs):
      instance.persons.save()

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
 