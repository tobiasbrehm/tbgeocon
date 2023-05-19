from django.db import models

# Create your models here.

class sub_section(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)
    text = models.TextField()
    text_de = models.TextField(blank=True)

    def __str__(self):
        return self.title



class logo(models.Model):
    title = models.CharField(max_length=50)  
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class section(models.Model):
    MAIN_SECTIONS = [
        ("about", "About", ),
        ("mining", "Mining & Geology", ),
        ("polar", "Polar Expeditions", ),
        ("photo", "Photography", ),
        ("translations", "Translations", ),
    ]
    title = models.CharField(choices = MAIN_SECTIONS, max_length=50)
    img = models.ImageField(upload_to='uploads', blank=True, null=True)
    img_alt = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    text_de = models.TextField(blank=True)
    sub_sections = models.ManyToManyField(sub_section, blank=True, null=True)   
    logos = models.ManyToManyField(logo, blank=True, null=True)

    def __str__(self):
        return self.title

