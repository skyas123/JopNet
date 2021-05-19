from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .models import User
from .models import Posts
from .models import Media
from .models import Dialogs
from .models import Message
from .models import Friends
from .forms import messageForm
from .forms import PersonsForms
from .forms import PostsForm
from .forms import ava
from .forms import photo
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def index(request):
  user=request.user
  news=Posts.objects.filter(author=user.pk)
  print(user.pk)

  if 'st' in request.POST:
      formava=ava(request.POST,request.FILES)
      if formava.is_valid() :
          #добавить удаление предыдущей аватарки
          avatar=formava.save()
          avatar.persons_set.add(user.persons)
  else:
     formava = ava 
  

  if 'submit' in request.POST:

   formpost=PostsForm(request.POST)
   formpicture=photo(request.POST,request.FILES)
   images=request.FILES.getlist('photo')
   if formpost.is_valid():

          post=formpost.save()
          user.persons.posts_set.add(post)

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
 

  return render(request,'JPT/home.html',{'user':user,'formpost':formpost,'formava':formava,'formpicture':formpicture,'news':news})

def news(request):
  user=request.user
  person=Persons.objects.get(user=user)
  listOfFriends=Persons.objects.filter(friends=person.pk)
  newsRoll=Posts.objects.filter(author__in=listOfFriends).exclude(author=person)

  if 'likebtn' in request.POST:
       a=request.POST.get('likebtn')
       nw=Posts.objects.get(pk=a)
       nw.like+=1
       nw.save()
       return HttpResponse(nw.like,
            content_type='html')


  return render(request, 'JPT/news.html',{"newsRoll":newsRoll})

def friends(request):
  user=request.user
  


  if 'find' in request.POST:
       req=request.POST.get('find')
       req=req.split()
      
       #не работают 100% совпадения по поиску доработать

       if not len(req):
        friendsList=User.objects.filter(persons__friends=user.pk)
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList,"user":user})
        return HttpResponse(response,content_type="html")

       else:
        friendsList=User.objects.filter(Q(first_name__in=req)|Q(last_name__in=req))
        response=render(request, 'JPT/resultSearch.html',{"friendsList":friendsList,"user":user})
        return HttpResponse(response,content_type="html")

  else:
       friendsList=User.objects.filter(persons__friends=user.pk)

      

  return render(request, 'JPT/friends.html',{"friendsList":friendsList,"user":user})

def dialogs(request):
    user=request.user
    dialogsList=Dialogs.objects.filter(listOfMembers=user.pk)
    return render(request,'JPT/dialogs.html',{"dialogsList":dialogsList,"persons":user})

def dialog(request, *args):
  dlgpk=args[0]
  user=request.user
  Dialogs.objects.get(pk=dlgpk)

  if  Dialogs.objects.get(Q(pk=dlgpk) and Q(listOfMembers=user.pk)): 
     messageList=Message.objects.filter(atachment=dlgpk)

  if "text" in request.POST:
      print(request.user)
      message=messageForm(request.POST)
      formpicture=photo(request.POST,request.FILES)
      images=request.FILES.getlist('photo')

      if message.is_valid():
           msg=message.save(commit=False)
           msg.atachment=Dialogs.objects.get(pk=dlgpk)
           msg.author=Persons.objects.get(pk=user.id)
           msg.save()

      if formpicture.is_valid():
       for p in images:
        picture=Media.objects.create(photo=p)
        #it doesn't clear shoud i use picture.save() or not
        msg.subphoto.add(picture)

  else:
      message=messageForm
      formpicture=photo

  return render(request,'JPT/dialog.html',{"messageList": messageList,"user":user,"message":messageForm,"formpicture":formpicture})

def guest(request, *args):
    user=request.user
    guestPK=args[0]
    guestInfo=User.objects.get(pk=guestPK)
    news=Posts.objects.filter(author=guestPK)
    
    if 'writeAmessage' in request.POST:
     try:
        Dialog=Dialogs.objects.get(Q(listOfMembers=guestPK) and Q(listOfMembers=user.pk))
        print(Dialog.pk)
     except Dialogs.DoesNotExist:
            Dialog=Dialogs.objects.create()
            Dialog.listOfMembers.add(user.persons)
            Dialog.listOfMembers.add(guestInfo.persons)
     return redirect('dialog', Dialog.pk)

    if 'addToFriend' in request.POST:
            FriendRequest=Friends.objects.create(Status=1)
            FriendRequest.pair.add(user.persons)
            FriendRequest.pair.add(guestInfo.persons)


      





    return render(request, 'JPT/guest.html',{"news":news,"guest":guestInfo})