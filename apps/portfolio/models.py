from django.db import models
from datetime import datetime
from apps.users.models import Role, Team

# # Create your models here.
class BaseProject(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        abstract = True
        
#project model
class Project(BaseProject):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('review', 'Under Review'),
        ('testing', 'Testing'),
        # ('deployment', 'Deployment'),
        ('updating', 'Updating'),
        ('pause', 'Pause'),
        ('maintenance', 'In Maintenance'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField( null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)
    intro = models.TextField()
    client = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True, default='hello@xxx.com')
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=False, blank=False, upload_to='projects')
    order = models.PositiveIntegerField(null=True, blank=True)
    remark = models.TextField(default='', blank=True)
    
    def change_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.save()
            
    def __str__(self):
        return self.name 
    
class ProjectCaseStudy(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='case_study') 
    thumbnail = models.ImageField(upload_to='projects/case_study', null=False, blank=False)
    industry = models.CharField(max_length=100)
    employee = models.CharField(max_length=12)
    website = models.URLField(max_length=100, default='https://', blank=True)
    short_desc = models.TextField()
    overview = models.TextField()
    challenge = models.TextField()
    solution_txt = models.TextField()
    solution_img1 = models.ImageField(upload_to='projects/case_study', default='defaults/default-img.jpg', blank=True, null=True)
    solution_img2 = models.ImageField(upload_to='projects/case_study', default='defaults/default-img.jpg', blank=True, null=True)
    result_txt = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project.name 
    
    
class ProjectTechnology(BaseProject):
    project_case_study = models.ForeignKey(ProjectCaseStudy, related_name='technologies', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ProjectRequirment(BaseProject):
    project_case_study = models.ForeignKey(ProjectCaseStudy, related_name='requirments', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ProjectResult(BaseProject):
    project_case_study = models.ForeignKey(ProjectCaseStudy, related_name='results', on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)  # e.g., efficiency, satisfaction, sales, cost
    percent = models.CharField(max_length=10, default='20%')  # or DecimalField for more precision
    up_or_down = models.CharField(max_length=10, blank=True)
    txt = models.TextField()
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    
    TESTIMONIAL_TYPE_CHOICES = [
        ('general', 'General'),
        ('project', 'Project Specific')
    ]
    
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=255, blank=True)
    testimonial_type = models.CharField(max_length=50, choices=TESTIMONIAL_TYPE_CHOICES, default='general')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='testimonials')
    comments = models.TextField()
    image = models.ImageField(upload_to='testimonial', default='defaults/user-icon.jpg', null=True, blank=True)
    
    order = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=False)
    

    def __str__(self):
        return self.full_name
    
    
    
# Project developer 
class ProjectDeveloper(BaseProject):
    name = models.ForeignKey(Team, related_name='projec_dev_name', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='project_name', on_delete=models.CASCADE)
    join_date = models.DateField()
    leave_date = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, related_name='project_role', on_delete=models.CASCADE)
    
    order = models.PositiveIntegerField(null=True, blank=True)
    remark = models.TextField(default='', blank=True)
    
    def __str__(self):
        return self.name.name
    

