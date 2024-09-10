from django import forms 
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit

from .models import Package, PackageFeature, Service

# form start here 
class PackageForm(forms.ModelForm):
    
    class Meta:
        model = Package
        fields = '__all__'
        
        
    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
       
       
# Package Feature Form  
class PackageFeatureForm(forms.ModelForm):
    
    class Meta:
        model = PackageFeature
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
        
        
# Service Form 
class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))