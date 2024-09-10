from django.urls import path
from . import views 


urlpatterns = [
    # path('<int:pk>/', views.resume_online, name='resume'),
    path('', views.resume_online, name='resume'),
    path('pdf/', views.resume_pdf, name='resume_pdf'),
    
    # try
    # path('venue_pdf/', views.venue_pdf, name='venue_pdf'),
    
    
    
    
    #resume urls 
    path('form/', views.resume_form, name='resume_form'),
    path('update/<int:pk>/', views.resume_form, name='resume_update'),
    path('resume/', views.resume, name='admin_resume'),
    
    # resume_experience 
    path('experiences/', views.resume_experience_all, name='resume_experience_all'),
    path('experiences/form/', views.resume_experience_form, name='resume_experience_form'),
    path('experiences/update/<int:pk>/', views.resume_experience_form, name='resume_experience_update'),
    path('experiences/delete/<int:pk>/', views.resume_experience_delete, name='resume_experience_delete'),
    
    # resume_experience_keys
    path('experiences/keys/', views.resume_experience_keys, name='resume_experience_keys'),
    path('experiences/keys/form', views.experience_keys_form, name='experience_keys_form'),
    path('experiences/keys/update/<int:pk>/', views.experience_keys_form, name='experience_keys_update'),
    path('experiences/keys/delete/<int:pk>/', views.experience_keys_delete, name='experience_keys_delete'),
    
    # resume projects
    path('projects/', views.resume_project_all, name='resume_project_all'),
    path('projects/form/', views.resume_project_form, name='resume_project_form'),
    path('projects/update/<int:pk>/', views.resume_project_form, name='resume_project_update'),
    path('projects/delete/<int:pk>/', views.resume_project_delete, name='resume_project_delete'),
    
    # resume_project_technologies
    path('projects/technologies/', views.resume_project_technologies, name='resume_project_technologies'),
    path('projects/technologies/form/', views.project_technology_form, name='project_technology_form'),
    path('projects/technologies/update/<int:pk>/', views.project_technology_form, name='project_technology_update'),
    path('projects/technologies/delete/<int:pk>/', views.project_technology_delete, name='project_technology_delete'),
    
    # technical_skill views 
    path('technical/skills/', views.technical_skill_all, name='technical_skill_all'),
    path('technical/skill/form/', views.technical_skill_form, name='technical_skill_form'),
    path('technical/skill/update/<int:pk>/', views.technical_skill_form, name='technical_skill_update'),
    path('technical/skill/delete/<int:pk>/', views.technical_skill_delete, name='technical_skill_delete'),
    
    # professional_skill_ view 
    path('professional/skills/', views.professional_skill_all, name='professional_skill_all'),
    path('professional/skill/form/', views.professional_skill_form, name='professional_skill_form'),
    path('professional/skill/update/<int:pk>/', views.professional_skill_form, name='professional_skill_update'),
    path('professional/skill/delete/<int:pk>/', views.professional_skill_delete, name='professional_skill_delete'),
    
    # resume_education view 
    path('educations/', views.resume_education_all, name='resume_education_all'),
    path('education/form/', views.resume_education_form, name='resume_education_form'),
    path('education/update/<int:pk>/', views.resume_education_form, name='resume_education_update'),
    path('education/delete/<int:pk>/', views.resume_education_delete, name='resume_education_delete'),
    
    # resume_award view 
    path('awards/', views.resume_award_all, name='resume_award_all'),
    path('award/form/', views.resume_award_form, name='resume_award_form'),
    path('award/update/<int:pk>/', views.resume_award_form, name='resume_award_update'),
    path('award/delete/<int:pk>/', views.resume_award_delete, name='resume_award_delete'),
    
    # resume_language_ view 
    path('languages/', views.resume_language_all, name='resume_language_all'),
    path('language/form/', views.resume_language_form, name='resume_language_form'),
    path('language/update/<int:pk>/', views.resume_language_form, name='resume_language_update'),
    path('language/delete/<int:pk>/', views.resume_language_delete, name='resume_language_delete'),
    
    # resume_interest view 
    path('interests/', views.resume_interest_all, name='resume_interest_all'),
    path('interest/form/', views.resume_interest_form, name='resume_interest_form'),
    path('interest/update/<int:pk>/', views.resume_interest_form, name='resume_interest_update'),
    path('interest/delete/<int:pk>/', views.resume_interest_delete, name='resume_interest_delete'),
    
]


