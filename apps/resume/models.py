from django.db import models

# Create your models here.
class BaseResume(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
        
        
class Resume(BaseResume):
    position = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    portfolio_url = models.URLField(max_length=20)
    address = models.CharField(max_length=100)
    image = models.ImageField()
    image_url = models.URLField(default='https://', blank=True, null=True)
    summary = models.TextField()
    
    linkedin_url = models.URLField(max_length=50, default='https://www.linkedin.com/in/amsbarik/')
    github_url = models.URLField(max_length=50, default='https://github.com/amsbarik')
    twitter_url = models.URLField(max_length=50, default='https://x.com/amsbarik')
    facebook_url = models.URLField(max_length=50, default='https://www.facebook.com/amsbarik')
    
    def __str__(self):
        return self.name
    
class ResumeExperience(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_experience', on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, default='year - year')
    role_desc = models.TextField()
    key_role_1 = models.CharField(max_length=100, blank=True, null=True)
    key_role_2 = models.CharField(max_length=100, blank=True, null=True)
    key_role_3 = models.CharField(max_length=100, blank=True, null=True)
    key_role_4 = models.CharField(max_length=100, blank=True, null=True)
    key_role_5 = models.CharField(max_length=100, blank=True, null=True)
    
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ResumeExperienceKey(BaseResume):
    resume_experience = models.ForeignKey(ResumeExperience, related_name='resume_experience_key', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class ResumeProject(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_project', on_delete=models.CASCADE)
    open_source_url = models.URLField(max_length=200, blank=True)
    project_live_url = models.URLField(max_length=200, blank=True)
    role_desc = models.TextField()
    
    technology_1 = models.CharField(max_length=50, blank=True, null=True)
    technology_2 = models.CharField(max_length=50, blank=True, null=True)
    technology_3 = models.CharField(max_length=50, blank=True, null=True)
    technology_4 = models.CharField(max_length=50, blank=True, null=True)
    technology_5 = models.CharField(max_length=50, blank=True, null=True)
    technology_6 = models.CharField(max_length=50, blank=True, null=True, default=None)
    technology_7 = models.CharField(max_length=50, blank=True, null=True, default=None)
    technology_8 = models.CharField(max_length=50, blank=True, null=True, default=None)
    technology_9 = models.CharField(max_length=50, blank=True, null=True, default=None)
    technology_10 = models.CharField(max_length=50, blank=True, null=True, default=None)
    
    order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class ResumeProjectTechnology(BaseResume):
    resume_project = models.ForeignKey(ResumeProject, related_name='resume_project_technology', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
   
class TechnicalSkill(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_technical_skill', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ProfessionalSkill(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_professional_skill', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ResumeEducation(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_education', on_delete=models.CASCADE)
    year = models.CharField(max_length=50, default='year - year')
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ResumeAward(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_award', on_delete=models.CASCADE)
    year = models.CharField(max_length=50, default='year')
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ResumeLanguage(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_language', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ResumeInterest(BaseResume):
    resume = models.ForeignKey(Resume, related_name='resume_interest', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name