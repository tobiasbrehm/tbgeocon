from django.contrib import admin
from .models import Sub_Section, Logo, Section

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    fields = ['title', 'img', 'img_preview', 'img_alt', 'text', 'text_de','sub_sections', 'logos']

class SubSectionAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    fields = ['title', 'img', 'img_preview', 'img_alt', 'text', 'text_de']

class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']   
    fields = ['title', 'img', 'img_preview', 'img_alt', 'weight'] 

admin.site.register(Section, SectionAdmin)
admin.site.register(Sub_Section, SubSectionAdmin)
admin.site.register(Logo, LogoAdmin)
