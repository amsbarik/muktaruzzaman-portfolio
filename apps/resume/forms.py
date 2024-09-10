
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import bleach
# from crispy_forms import helper
# from crispy_forms.layout import Layout


from .models import Resume, ResumeExperience, ResumeExperienceKey, ResumeProject, ResumeProjectTechnology, TechnicalSkill, ProfessionalSkill, ResumeEducation, ResumeAward, ResumeLanguage, ResumeInterest

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        
    def clean_content(self):
        summary = self.cleaned_data.get('summary')
        allowed_tags = ['span']
        allowed_attributes = {'span': [ 'class']}
        sanitized_content = bleach.clean(summary, tags=allowed_tags, attributes=allowed_attributes)
        return sanitized_content

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['summary'].widget.attrs.update({'rows': 5})
        # self.fields['name'].required = False
        

class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = ResumeExperience
        fields = '__all__'
        
    def clean_content(self):
        role_desc = self.cleaned_data.get('role_desc')
        allowed_tags = ['span']
        allowed_attributes = {'span': [ 'class']}
        sanitized_content = bleach.clean(role_desc, tags=allowed_tags, attributes=allowed_attributes)
        return sanitized_content

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
    
        
        
        

class ResumeExperienceKeyForm(forms.ModelForm):
    class Meta:
        model = ResumeExperienceKey
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume_experience'].empty_label = 'Select Experience'


class ResumeProjectForm(forms.ModelForm):
    class Meta:
        model = ResumeProject
        fields = '__all__'
        
    def clean_content(self):
        role_desc = self.cleaned_data.get('role_desc')
        allowed_tags = ['span']
        allowed_attributes = {'span': [ 'class']}
        sanitized_content = bleach.clean(role_desc, tags=allowed_tags, attributes=allowed_attributes)
        return sanitized_content

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        
    
        


class ResumeProjectTechnologyForm(forms.ModelForm):
    class Meta:
        model = ResumeProjectTechnology
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume_project'].empty_label = 'Select Project'
        


class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        


class ProfessionalSkillForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSkill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        


class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = ResumeEducation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        


class ResumeAwardForm(forms.ModelForm):
    class Meta:
        model = ResumeAward
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        
        

class ResumeLanguageForm(forms.ModelForm):
    class Meta:
        model = ResumeLanguage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        
        

class ResumeInterestForm(forms.ModelForm):
    class Meta:
        model = ResumeInterest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['resume'].empty_label = 'Select Resume'
        
    



        




  