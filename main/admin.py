from django.contrib import admin
from .models import sub_section, logo, section

# Register your models here.


admin.site.register(section)
admin.site.register(sub_section)
admin.site.register(logo)
