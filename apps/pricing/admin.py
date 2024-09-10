from django.contrib import admin
from .models import Package, Service

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
admin.site.register(Package, PackageAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
admin.site.register(Service, ServiceAdmin)