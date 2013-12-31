import datetime
from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=300)
    message = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    
    def unicode(self):
        return self.email
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = ('Contact Us')
        verbose_name_plural = ('Contacted Us')
        
    
