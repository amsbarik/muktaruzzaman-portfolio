from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # skill icons 
    path('skill/icons/', views.skill_icon_all, name='skill_icon_all'),
    path('skill/icons/form/', views.skill_icon_form, name='skill_icon_form'),
    path('skill/icons/update/<int:pk>/', views.skill_icon_form, name='skill_icon_update'),
    path('skill/icons/delete/<int:pk>/', views.skill_icon_delete, name='skill_icon_delete'),
    
    # skills 
    path('skills/', views.skill_all, name='skill_all'),
    path('skill/form/', views.skill_form, name='skill_form'),
    path('skill/update/<int:pk>/', views.skill_form, name='skill_update'),
    path('skill/delete/<int:pk>/', views.skill_delete, name='skill_delete'),
    
    
]
