from django.db import models

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    short_desc = models.TextField()
    revisions = models.CharField(max_length=6)
    delivery_time = models.CharField(max_length=20, default='7 days')
    
    order = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
 
#  Package Fetures 
class PackageFeature(models.Model):
    title = models.CharField(max_length=20)   
    short_desc = models.TextField(blank=True)
    
    standard = models.BooleanField(default=True)
    premium = models.BooleanField(default=True)
    bussiness = models.BooleanField(default=True)
    
    order = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.TextField()
    thumbnail = models.ImageField(default='defaults/mouse.png', upload_to='services/')
    
    order = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
