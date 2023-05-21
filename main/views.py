from django.shortcuts import render
from .models import Section
from .forms import ContactForm_de

# Create your views here.

def home (request):
    sections = []
    about = Section.objects.get(title = 'about')
    mining = Section.objects.get(title = 'mining')
    polar = Section.objects.get(title = 'polar')
    photo = Section.objects.get(title = 'photo')
    translations = Section.objects.get(title = 'translations')
    contact = Section.objects.get(title = 'contact')
    sections.append(mining)
    sections.append(polar)
    sections.append(photo)
    sections.append(translations)
    form_de = ContactForm_de()
    return render (request,'home.html', {'about': about, 'mining': mining,'polar': polar,'photo': photo,'translations': translations,'contact': contact, 'sections': sections, 'form_de': form_de})