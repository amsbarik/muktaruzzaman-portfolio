from django.db import models
from apps.pricing.models import Service
from datetime import date, timedelta , datetime

# Create your models here.
class Contact(models.Model):
    STATUS_CHOICES = [
        ('un_read', 'Un-read'),
        ('read', 'Read'),
        ('contact', 'Contacted'),
        ('on_hold', 'On Hold'),
        ('follow_up', 'Follow-up'),
        ('confirm', 'Confirm'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='un_read')
    
    name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=400)
    budget = models.DecimalField(max_digits=12, decimal_places=2,  default=0.00, null=True, blank=True) 
    deadline = models.DateField(default=date.today() + timedelta(weeks=4), null=True, blank=True)
    message = models.TextField()
    
    remark = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
    
    def change_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.save()
            
    def __str__(self):
        return self.name
    
    
    