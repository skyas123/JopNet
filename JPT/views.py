from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .models import Media
from .forms import PersonsForms
from .forms import ava


# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=4)
  

  if request.method == 'POST':

   form=ava(request.POST,request.FILES)
   
   if form.is_valid():
          avatar=form.save()
          avatar.persons_set.add(persons)
   
         
           
     
  else:
     form = ava 

  return render(request, 'JPT/home.html',{'persons':persons,'form': form})

def news(request):
  return render(request, 'JPT/news.html')

