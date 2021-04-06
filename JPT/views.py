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


# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=8)
  news=Posts.objects.filter(author=persons.pk)

  if 'st' in request.POST:
      formava=ava(request.POST,request.FILES)
      if formava.is_valid() :
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
       print(request.POST)
       a=request.POST.get('likebtn')
       nw=Posts.objects.get(pk=a)
       nw.like+=1
       nw.save()
       return HttpResponse(nw.like,
            content_type='html')
 

  return render(request,'JPT/home.html',{'persons':persons,'formpost':formpost,'formava':formava,'formpicture':formpicture,'news':news})

def news(request):
  return render(request, 'JPT/news.html')

