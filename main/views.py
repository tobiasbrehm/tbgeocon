from django.shortcuts import render
from .models import section

# Create your views here.

def home (request):
    sections = section.objects.all()
    return render (request,'home.html', {'sections': sections})