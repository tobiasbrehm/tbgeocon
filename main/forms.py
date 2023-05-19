from django import forms

class ContactForm_de(forms.Form):
    SALUTATION = [
        ('mr', 'Herr'),
        ('mrs', 'Frau'),
        ('else', 'Andere'),
    ]
    salutation = forms.CharField(label='Anrede', max_length=4, widget=forms.Select(choices=SALUTATION))
    prename = forms.CharField(label='Vorname', max_length=100, required=True)
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='E-Mail', max_length=254, required=True)
    message = forms.CharField(label='Nachricht', widget=forms.Textarea, required=True)
