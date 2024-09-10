from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div

from .models import Project, ProjectCaseStudy, ProjectTechnology, ProjectRequirment, ProjectResult, Testimonial, ProjectDeveloper

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__' 
        
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
            'end_date' : forms.DateInput(attrs={'type': 'date'}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('submit', 'Save'))
            

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['status', 'remark']
        
    

class ProjectCaseStudyForm(forms.ModelForm):
    class Meta:
        model = ProjectCaseStudy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project'].empty_label = 'Select Project'


class ProjectTechnologyForm(forms.ModelForm):
    class Meta:
        model = ProjectTechnology
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project_case_study'].empty_label = 'Select Project'


class ProjectRequirmentForm(forms.ModelForm):
    class Meta:
        model = ProjectRequirment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project_case_study'].empty_label = 'Select Project'


class ProjectResultForm(forms.ModelForm):
    class Meta:
        model = ProjectResult
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project_case_study'].empty_label = 'Select Project'





# Testimonial form 
# class TestimonialForm(forms.ModelForm):
#     TESTIMONIAL_TYPE_CHOICES = [
#         ('general', 'General'),
#         ('project_specific', 'Project-Specific')
#     ]

#     testimonial_type = forms.ChoiceField(choices=TESTIMONIAL_TYPE_CHOICES, widget=forms.RadioSelect)
#     project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

#     class Meta:
#         model = Testimonial
#         fields = ['full_name', 'position', 'testimonial_type', 'project', 'image', 'comments', 'is_active']

#     def clean(self):
#         cleaned_data = super().clean()
#         testimonial_type = cleaned_data.get('testimonial_type')
#         project = cleaned_data.get('project')

#         if testimonial_type == 'project_specific' and not project:
#             self.add_error('project', 'This field is required for project-specific testimonials.')

#         return cleaned_data



class TestimonialForm(forms.ModelForm):
    TESTIMONIAL_TYPE_CHOICES = [
        ('general', 'General'),
        ('project', 'Project Specific')
    ]

    testimonial_type = forms.ChoiceField(choices=TESTIMONIAL_TYPE_CHOICES, widget=forms.RadioSelect, initial='general')
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Testimonial
        fields = ['full_name', 'position', 'testimonial_type', 'project', 'image', 'comments', 'order', 'is_active']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project'].empty_label = 'Select Project'

        
    def clean(self):
        cleaned_data = super().clean()
        testimonial_type = cleaned_data.get('testimonial_type')
        project = cleaned_data.get('project')

        if testimonial_type == 'project' and not project:
            self.add_error('project', 'This field is required for a specific project testimonial.')

        return cleaned_data
    
    
   
# Feedback Form
class FeedbackForm(forms.ModelForm):
    
    TESTIMONIAL_TYPE_CHOICES = [
        ('general', 'General'),
        ('project', 'Project Specific')
    ]

    testimonial_type = forms.ChoiceField(choices=TESTIMONIAL_TYPE_CHOICES, widget=forms.RadioSelect, initial='general')
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    
    class Meta:
        model = Testimonial
        fields = ['full_name', 'position', 'testimonial_type', 'project', 'comments', 'image']
        
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'position': forms.TextInput(attrs={'placeholder': 'Enter your job position'}),
            'comments': forms.Textarea(attrs={'placeholder': 'Write your feedback here...'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project'].empty_label = 'Select Project'
        self.fields['full_name'].label = "Full Name"
        self.fields['position'].label = "Job Position"
        self.fields['image'].label = "Your Photo"
        self.fields['comments'].label = "Feedback"

        
    def clean(self):
        cleaned_data = super().clean()
        testimonial_type = cleaned_data.get('testimonial_type')
        project = cleaned_data.get('project')

        if testimonial_type == 'project' and not project:
            self.add_error('project', 'This field is required for a specific project testimonial.')

        return cleaned_data


# ProjectDeveloperForm
class ProjectDeveloperForm(forms.ModelForm):
    class Meta:
        model = ProjectDeveloper
        fields = ['project', 'name', 'role', 'join_date', 'leave_date', 'remark', 'order', 'is_active']
    
        widgets = {
            'join_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'leave_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
    #this Ensure that ProjectDeveloperForm allows the project field to be dynamically filtered
    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('project_id', None)
        super(ProjectDeveloperForm, self).__init__(*args, **kwargs)
        
        if project_id:
            self.fields['project'].queryset = Project.objects.filter(id=project_id)
        else:
            self.fields['project'].queryset = Project.objects.all()
            
        
        # super().__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))
        self.fields['project'].empty_label = 'Select Project'
        self.fields['name'].empty_label = 'Select Developer'
        self.fields['role'].empty_label = 'Select Role'
            
            
