from django.shortcuts import render
from .models import section
from .forms import ContactForm_de

# Create your views here.

def home (request):
    sections = section.objects.all()
    form_de = ContactForm_de()
    return render (request,'home.html', {'sections': sections, 'form_de': form_de})