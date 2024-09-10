from django.contrib import admin
from .models import Project, ProjectCaseStudy, ProjectTechnology, ProjectRequirment, ProjectResult, ProjectDeveloper

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'name', 'intro', 'client', 'image', 'is_active',)

admin.site.register(Project, ProjectAdmin) 


class ProjectCaseStudyAdmin(admin.ModelAdmin):
    list_display = ('project', 'thumbnail', 'industry', 'employee', 'website', 'short_desc', 'overview', 'challenge', 'solution_txt', 'solution_img1', 'solution_img2', 'result_txt')
    
admin.site.register(ProjectCaseStudy, ProjectCaseStudyAdmin)


class ProjectTechnologyAdmin(admin.ModelAdmin):
	list_display = ('name', 'project_case_study')

admin.site.register(ProjectTechnology, ProjectTechnologyAdmin) 

class ProjectRequirmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'project_case_study')

admin.site.register(ProjectRequirment, ProjectRequirmentAdmin) 

class ProjectResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'up_or_down', 'txt', 'project_case_study')
    
admin.site.register(ProjectResult, ProjectResultAdmin)


class ProjectDeveloperAdmin(admin.ModelAdmin):
    list_display = ('join_date', 'leave_date',  'name', 'project', 'role', 'remark')
    
admin.site.register(ProjectDeveloper, ProjectDeveloperAdmin)