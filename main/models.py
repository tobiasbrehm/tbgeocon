from django.db import models

# Create your models here.

class sub_section(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)
    text = models.TextField()
    text_de = models.TextField(blank=True)

class logo(models.Model):
    title = models.CharField(max_length=50)  
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)

class section(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads', blank=True, null=True)
    img_alt = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    text_de = models.TextField(blank=True)
    sub_sections = models.ForeignKey(sub_section, on_delete=models.CASCADE, blank=True, null=True)   
    logos = models.ForeignKey(logo, on_delete=models.CASCADE, blank=True, null=True)

