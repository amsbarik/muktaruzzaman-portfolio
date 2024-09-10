from django.db import models

# Create your models here.
class BaseAbout(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    

class SkillIcon(BaseAbout):
    icon_class = models.CharField(max_length=50)
    
    def __str__(self):
        return self.icon_class
    
class Skill(BaseAbout):
    icon_1 = models.ForeignKey(SkillIcon, related_name='icon_1', on_delete=models.CASCADE, blank=True, null=True)
    icon_2 = models.ForeignKey(SkillIcon, related_name='icon_2', on_delete=models.CASCADE, blank=True, null=True)
    icon_3 = models.ForeignKey(SkillIcon, related_name='icon_3', on_delete=models.CASCADE, blank=True, null=True)
    
    logo_1 = models.ImageField(blank=True, null=True, upload_to='skill_logo')
    logo_2 = models.ImageField(blank=True, null=True, upload_to='skill_logo')
    logo_3 = models.ImageField(blank=True, null=True, upload_to='skill_logo')
    
    skill_txt = models.TextField()
    order = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    