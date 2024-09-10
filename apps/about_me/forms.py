from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Skill, SkillIcon

# create form here 
class SkillIconForm(forms.ModelForm):
    
    class Meta:
        model = SkillIcon
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        


class SkillForm(forms.ModelForm):
    
    class Meta:
        model = Skill
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'save'))
        self.fields['icon_1'].empty_label = 'Select icon 1'
        self.fields['icon_2'].empty_label = 'Select icon 2'
        self.fields['icon_3'].empty_label = 'Select icon 3'
        
    