from django.shortcuts import render
from django.http import HttpResponse
from .models import Persons

# Create your views here.
def index(request):
  persons=Persons.objects.get(pk=1)
  return render(request, 'JPT/home.html',{'persons':persons})

def news(request):
  return render(request, 'JPT/news.html')

