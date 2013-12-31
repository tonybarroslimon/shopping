from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactUs
    
admin.site.register(ContactUs, ContactUsAdmin)
