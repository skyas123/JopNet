from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Persons
from .forms import PersonsForms
from .forms import ava


# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=1)
  

  if request.method == 'POST':

   form=ava(request.POST,request.FILES,instance=persons,auto_id='')
   
   if form.is_valid(): 
            form.save()        
  else:
     form = ava(auto_id='') 

  return render(request, 'JPT/home.html',{'persons':persons,'form': form})

def news(request):
  return render(request, 'JPT/news.html')

