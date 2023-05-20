from django.shortcuts import render
from .models import section
from .forms import ContactForm_de

# Create your views here.

def home (request):
    sections = []
    about = section.objects.get(title = 'about')
    mining = section.objects.get(title = 'mining')
    polar = section.objects.get(title = 'polar')
    photo = section.objects.get(title = 'photo')
    translations = section.objects.get(title = 'translations')
    contact = section.objects.get(title = 'contact')
    sections.append(mining)
    sections.append(polar)
    sections.append(photo)
    sections.append(translations)
    form_de = ContactForm_de()
    return render (request,'home.html', {'about': about, 'mining': mining,'polar': polar,'photo': photo,'translations': translations,'contact': contact, 'sections': sections, 'form_de': form_de})