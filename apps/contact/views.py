# from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.users.views import is_superuser
from .models import Contact
from apps.pricing.models import Service
from .forms import ContactStatusForm

# Create your views here.
def contact(request):
    services = Service.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        service_id = request.POST.get('service')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        budget = request.POST.get('budget')
        deadline = request.POST.get('deadline')
        message = request.POST.get('message')
       
        # validate the data 
        if name and service_id and mobile and email and deadline and budget and message:
            service = Service.objects.get(id=service_id)
            Contact.objects.create(
                name=name,
                service=service,
                mobile=mobile,
                email=email,
                address=address,
                budget = budget,
                deadline = deadline,
                message=message,
            )
            
            messages.success(request, 'Your message has been sent successfully! Thank You')
            return redirect('contact')
        
    return render(request, 'contact/contact.html', {'services': services})



# ///////////// admin message view here ////////////

# messages 
@login_required
@user_passes_test(is_superuser)
def client_messages(request):
    
    messages = Contact.objects.all()
    
    return render(request, 'admin_panel/messages/messages.html', {'messages': messages})



@login_required
@user_passes_test(is_superuser)
def message_status_update(request, contact_id):
    
    messages = Contact.objects.all()
    message = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactStatusForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Message status updated successfully.')
            return redirect('messages')
        
    else:
        form = ContactStatusForm(instance=message)
    
    return render(request, 'admin_panel/messages/messages.html', {'form': form, 'messages': messages})
