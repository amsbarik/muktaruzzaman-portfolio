from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import Blog, BlogContent, Subscribe, Tag, Category, Comment 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['category'].empty_label = 'Select Category'
        
        

# blog content form 
class BlogContentForm(forms.ModelForm):
    
    class Meta:
        model = BlogContent
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'save'))
        self.fields['blog'].empty_label = 'Select Blog'
        
        
class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'save'))