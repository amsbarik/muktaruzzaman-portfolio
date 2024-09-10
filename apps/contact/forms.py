from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div

from .models import Contact



class ContactStatusForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['remark', 'status']
        
        widgets ={
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'status' : forms.ChoiceField(attrs={'class': 'form-control'}),
        }
        
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.form_method = 'POST'
        #     self.helper.add_input(Submit('submit', 'Save'))
            
            
    