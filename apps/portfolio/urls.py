from django.urls import path
from . import views 

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('case-study/<int:pk>/', views.case_study, name='case_study'),
    path('feedback/', views.feedback, name='feedback'),
    
    # testimonial_form 
    path('testimonials', views.testimonial_all, name='testimonial_all'),
    path('testimonial/form/', views.testimonial_form, name='testimonial_form'),
    path('testimonial/update/<int:pk>/', views.testimonial_form, name='testimonial_update'),
    path('testimonial/delete/<int:pk>/', views.testimonial_delete, name='testimonial_delete'),
    
    
    
    
    # admin projects urls start 
    # project views 
    path('all/', views.project_all, name='project_all'),
    path('add/', views.project_form, name='project_form'),
    path('update/<int:pk>', views.project_form, name='project_update'),
    path('project/delete/<int:pk>', views.project_delete, name='project_delete'),
    
    path('status/<str:status>/', views.projects_by_status, name='projects_by_status'),
    
    # path('view/<int:pk>/', views.project_view, name='project_view'),
    path('view/<int:project_id>/', views.project_view, name='project_view'),
    path('developer/assign/<int:project_id>/', views.developer_assign, name='developer_assign'),
    path('developer/update/<int:dev_id>/', views.developer_assign, name='developer_update'),
    
    # project_case_study urls start
    path('case/studies/', views.project_case_study_all, name='project_case_study_all'),
    path('case-study/form/', views.project_case_study_form, name='project_case_study_form'),
    path('case-study/update/<int:pk>/', views.project_case_study_form, name='project_case_study_update'),
    
    # technologies
    path('technologies/', views.project_technology_all, name='projects_technology_all'),
    path('technology/form/', views.project_technology_form, name='projects_technology_form'),
    path('technology/update/<int:pk>/', views.project_technology_form, name='projects_technology_update'),
    path('technology/delete/<int:pk>/', views.project_technology_delete, name='projects_technology_delete'),
    
    # requirments
    path('requirments/', views.project_requirment_all, name='project_requirment_all'),
    path('requirment/form/', views.project_requirment_form, name='project_requirment_form'),
    path('requirment/update/<int:pk>/', views.project_requirment_form, name='project_requirment_update'),
    path('requirment/delete/<int:pk>/', views.project_requirment_delete, name='project_requirment_delete'),
    
    # results
    path('results/', views.project_result_all, name='project_result_all'),
    path('result/form/', views.project_result_form, name='project_result_form'),
    path('result/update/<int:pk>/', views.project_result_form, name='project_result_update'),
    path('result/delete/<int:pk>/', views.project_result_delete, name='project_result_delete'),
    
    
    
    
    
    
    
    
    
    
    
    # user app urls 
    path('developers/', views.developer_all, name='developer_all'),
    path('developer/add/', views.developer_add, name='developer_add'),
    path('developer/update/<int:pk>/', views.developer_update, name='developer_update'),
    path('developer/delete/<int:pk>', views.developer_delete, name='developer_delete'),
]


