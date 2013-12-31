from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image1 = models.ImageField(upload_to='product_images', blank=True, null=True)
    price = models.FloatField(default=0.00)
    sku = models.CharField(max_length=160, default='abc')
    inventory = models.IntegerField(default=0)
        
    def __unicode__(self):
        return self.name
    
    class meta:
        ordering = ['-id']
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        
        
    