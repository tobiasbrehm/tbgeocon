from django.shortcuts import render
from .models import Section
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.core.mail import get_connection, send_mail
from django.template.loader import render_to_string
from django. conf import settings
from .forms import ContactForm, ContactForm_de

# Create your views here.

def home (request):
    sections = []
    about = Section.objects.get(title = 'about')
    mining = Section.objects.get(title = 'mining')
    polar = Section.objects.get(title = 'polar')
    photo = Section.objects.get(title = 'photo')
    translations = Section.objects.get(title = 'translations')
    contact = Section.objects.get(title = 'contact')
    impressum = Section.objects.get(title = 'impressum')
    legal = Section.objects.get(title = 'legal')
    sections.append(mining)
    sections.append(polar)
    sections.append(photo)
    sections.append(translations) 

    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form_de = ContactForm_de(request.POST)

        if form.is_valid() or form_de.is_valid():
            cd = form.cleaned_data
            subject, from_email, to = 'TB Geocon Kontaktformular Nachricht', settings.EMAIL_HOST_USER, 'info@tbgeocon.com'
            html_content = render_to_string('email.html', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ContactForm()
        form_de = ContactForm_de()
        if 'submitted' in request.GET:
            submitted = True
    return render (request,'home.html', {'about': about, 'mining': mining,'polar': polar,'photo': photo,'translations': translations,'contact': contact, 'sections': sections, 'form_de': form_de, 'form': form, 'submitted': submitted, 'impressum': impressum, 'legal': legal})
