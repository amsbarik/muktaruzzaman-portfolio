from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from apps.users.views import is_superuser

from .forms import PackageForm, PackageFeatureForm, ServiceForm
from .models import Package, PackageFeature, Service

# Create your views here.
def pricing(request):
    
    services = Service.objects.filter(is_active=True).order_by('order', 'created_at').all()
    packages = Package.objects.filter(is_active=True).order_by('order', 'created_at')[:3]
    package_features = PackageFeature.objects.filter(is_active=True).order_by('order', 'created_at').all()
    
    context = {
        'services': services,
        'packages': packages,
        'package_features': package_features,
    }
    
    return render(request, 'pricing/pricing.html', context)



# admin view start here 
@login_required
@user_passes_test(is_superuser)
def service_all(request):
    services = Service.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/pricing/service_all.html', {'services': services})


# service create and update form 
@login_required
@user_passes_test(is_superuser)
def service_form(request, service_id=0):
    
    if request.method == 'GET':
        if service_id == 0:
            form = ServiceForm()
        else:
            service = get_object_or_404(Service, id=service_id)
            form = ServiceForm(instance=service)
            
        return render(request, 'admin_panel/pricing/service_form.html', {'form': form})
    
    else:
        if service_id == 0:
            form = ServiceForm(request.POST, request.FILES)
        else:
            service = get_object_or_404(Service, id=service_id)
            form = ServiceForm(request.POST, request.FILES, instance=service)
            
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Service Create Successfully!')
            
        return redirect('service_all')
    
    
# service delete 
@login_required
@user_passes_test(is_superuser)
def service_delete(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect('service_all')
            
            
            

# package view 
@login_required
@user_passes_test(is_superuser)
def package_all(request):
    packages = Package.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/pricing/package_all.html', {'packages': packages})


# package create and update form 
@login_required
@user_passes_test(is_superuser)
def package_form(request, package_id=0):
    
    if request.method == 'GET':
        if package_id == 0:
            form = PackageForm()
        else:
            package = get_object_or_404(Package, id=package_id)
            form = PackageForm(instance=package)
            
        return render(request, 'admin_panel/pricing/package_form.html', {'form': form})
    
    else:
        if package_id == 0:
            form = PackageForm(request.POST)
        else:
            package = get_object_or_404(Package, id=package_id)
            form = PackageForm(request.POST, instance=package)
            
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Package Create Successfully!')
            
        return redirect('package_all')
    
    
# package delete 
@login_required
@user_passes_test(is_superuser)
def package_delete(request, package_id):
    package = Package.objects.get(id=package_id)
    package.delete()
    return redirect('package_all')
            
            

# package feature view 
@login_required
@user_passes_test(is_superuser)
def package_feature_all(request):
    package_features = PackageFeature.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/pricing/package_feature_all.html', {'package_features': package_features})


# package feature create and update form 
@login_required
@user_passes_test(is_superuser)
def package_feature_form(request, feature_id=0):
    
    if request.method == 'GET':
        if feature_id == 0:
            form = PackageFeatureForm()
        else:
            package_feature = get_object_or_404(PackageFeature, id=feature_id)
            form = PackageFeatureForm(instance=package_feature)
            
        return render(request, 'admin_panel/pricing/package_feature_form.html', {'form': form})
    
    else:
        if feature_id == 0:
            form = PackageFeatureForm(request.POST)
        else:
            package_feature = get_object_or_404(PackageFeature, id=feature_id)
            form = PackageFeatureForm(request.POST, instance=package_feature)
            
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Package Feature Create Successfully!')
            
        return redirect('package_feature_all')
    
    
# package feature delete 
@login_required
@user_passes_test(is_superuser)
def package_feature_delete(request, feature_id):
    package_feature = PackageFeature.objects.get(id=feature_id)
    package_feature.delete()
    return redirect('package_feature_all')
            
            