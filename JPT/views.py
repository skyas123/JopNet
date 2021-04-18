from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .models import Posts
from .models import Media
from .forms import PersonsForms
from .forms import PostsForm
from .forms import ava
from .forms import photo
from .forms import  searchform
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=9)
  news=Posts.objects.filter(author=persons.pk)

  if 'st' in request.POST:
      formava=ava(request.POST,request.FILES)
      if formava.is_valid() :
          #добавить удаление предыдущей аватарки
          avatar=formava.save()
          avatar.persons_set.add(persons)
  else:
     formava = ava 
  

  if 'submit' in request.POST:

   formpost=PostsForm(request.POST)
   formpicture=photo(request.POST,request.FILES)
   images=request.FILES.getlist('photo')
   if formpost.is_valid():

          post=formpost.save()
          persons.posts_set.add(post)

   if formpicture.is_valid():

     for p in images:
      picture=Media.objects.create(photo=p)
      #it doesn't clear shoud i use picture.save() or not
      post.subphoto.add(picture)
  else:
     formpost = PostsForm
     formpicture=photo
  
  if 'likebtn' in request.POST:
       a=request.POST.get('likebtn')
       nw=Posts.objects.get(pk=a)
       nw.like+=1
       nw.save()
       return HttpResponse(nw.like,
            content_type='html')

  if 'deletenw' in request.POST:
       a=request.POST.get('deletenw')
       #здесь обработку на случай отсутствия объекта
       Posts.objects.get(pk=a).delete()
       answr=100
       return HttpResponse(answr,
            content_type='html')
 

  return render(request,'JPT/home.html',{'persons':persons,'formpost':formpost,'formava':formava,'formpicture':formpicture,'news':news})

def news(request):
  persons=Persons.objects.get(pk=9)
  listOfFriends=Persons.objects.filter(friends=persons.pk)
  newsRoll=Posts.objects.filter(author__in=listOfFriends)

  if 'likebtn' in request.POST:
       a=request.POST.get('likebtn')
       nw=Posts.objects.get(pk=a)
       nw.like+=1
       nw.save()
       return HttpResponse(nw.like,
            content_type='html')


  return render(request, 'JPT/news.html',{"newsRoll":newsRoll})

def friends(request):
  persons=Persons.objects.get(pk=9)
  


  if 'find' in request.POST:
       req=request.POST.get('find')
       req=req.split()
       print(len(req))

       if not len(req):
        print('1 block')
        friendsList=Persons.objects.filter(friends=persons.pk)
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList})
        return HttpResponse(response,content_type="html")

       else:
        print('2 block')
        friendsList=Persons.objects.filter(Q(first_name__in=req)|Q(second_name__in=req))
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList})
        return HttpResponse(response,content_type="html")

  else:
       friendsList=Persons.objects.filter(friends=persons.pk)
       

  return render(request, 'JPT/friends.html',{"friendsList":friendsList})