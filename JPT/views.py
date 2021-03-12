from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .models import Posts
from .models import Media
from .forms import PersonsForms
from .forms import PostsForm
from .forms import ava


# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=7)
  
  if 'st' in request.POST:
      print(request.POST)
      formava=ava(request.POST,request.FILES)
      if formava.is_valid() :
          avatar=formava.save()
          avatar.persons_set.add(persons)
  else:
     formava = ava 
  

  if 'submit' in request.POST:
   print(request.POST)
   formpost=PostsForm(request.POST,request.FILES)
   if formpost.is_valid():
          post=formpost.save()
          persons.posts_set.add(post)
  else:
     formpost = PostsForm
     


  return render(request,'JPT/home.html',{'persons':persons,'formpost':formpost,'formava':formava})

def news(request):
  return render(request, 'JPT/news.html')

