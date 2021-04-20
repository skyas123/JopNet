from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .models import Posts
from .models import Media
from .models import Dialogs
from .models import Message
from .forms import PersonsForms
from .forms import PostsForm
from .forms import ava
from .forms import photo
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=8)
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
  persons=Persons.objects.get(pk=8)
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
  persons=Persons.objects.get(pk=8)
  


  if 'find' in request.POST:
       req=request.POST.get('find')
       req=req.split()
      
       #не работают 100% совпадения по поиску доработать

       if not len(req):
        friendsList=Persons.objects.filter(friends=persons.pk)
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList})
        return HttpResponse(response,content_type="html")

       else:
        friendsList=Persons.objects.filter(Q(first_name__in=req)|Q(second_name__in=req))
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList})
        return HttpResponse(response,content_type="html")

  else:
       friendsList=Persons.objects.filter(friends=persons.pk)
       

  return render(request, 'JPT/friends.html',{"friendsList":friendsList})

def dialogs(request):
    persons=Persons.objects.get(pk=8)
    dialogsList=Dialogs.objects.filter(listOfMembers=persons.pk)
    return render(request,'JPT/dialogs.html',{"dialogsList":dialogsList,"persons":persons})

def dialog(request, *args):
    dlgpk=args[0]
    prsnl=args[1]
    persons=Persons.objects.get(pk=prsnl)
    messageList=Message.objects.filter(atachment=dlgpk)
    
    return render(request,'JPT/dialog.html',{"messageList": messageList,"persons":persons})