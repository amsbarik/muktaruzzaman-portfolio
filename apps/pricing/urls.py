from django.urls import path
from . import views 

urlpatterns = [
    path('', views.pricing, name='pricing'),
    
    # service urls 
    path('all/', views.service_all, name='service_all'),
    path('form/', views.service_form, name='service_form'),
    path('update/<int:service_id>/', views.service_form, name='service_update'),
    path('delete/<int:service_id>/', views.service_delete, name='service_delete'),
    
    # package urls 
    path('packages/', views.package_all, name='package_all'),
    path('package/form/', views.package_form, name='package_form'),
    path('package/update/<int:package_id>/', views.package_form, name='package_update'),
    path('package/delete/<int:package_id>/', views.package_delete, name='package_delete'),
    
    # package feature urls 
    path('package/features/', views.package_feature_all, name='package_feature_all'),
    path('package/feature/form/', views.package_feature_form, name='package_feature_form'),
    path('package/feature/update/<int:feature_id>/', views.package_feature_form, name='package_feature_update'),
    path('package/feature/delete/<int:feature_id>/', views.package_feature_delete, name='package_feature_delete'),
]
