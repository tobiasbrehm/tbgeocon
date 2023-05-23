from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Sub_Section(models.Model):
    title = models.CharField(max_length=50)
    title_de = models.CharField(max_length=50, blank=True)
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)
    text = models.TextField()
    text_de = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
    
    class Meta:
        verbose_name = "Sub section"
        verbose_name_plural = "Sub sections"


class Logo(models.Model):
    title = models.CharField(max_length=50)  
    img = models.ImageField(upload_to='uploads')
    img_alt = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)

    class Meta: 
        ordering = ['weight']
        
    def __str__(self):
        return self.title
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')


class Section(models.Model):
    MAIN_SECTIONS = [
        ("about", "About", ),
        ("mining", "Mining & Geology", ),
        ("polar", "Polar Expeditions", ),
        ("photo", "Photography", ),
        ("translations", "Translations", ),
        ("contact", "Contact", ),
    ]
    title = models.CharField(choices = MAIN_SECTIONS, max_length=50)
    img = models.ImageField(upload_to='uploads', blank=True, null=True)
    img_alt = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    text_de = models.TextField(blank=True)
    sub_sections = models.ManyToManyField(Sub_Section, blank=True)   
    logos = models.ManyToManyField(Logo, blank=True)

    def __str__(self):
        return self.get_title_display()
    
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
