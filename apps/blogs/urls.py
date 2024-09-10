from django.urls import path
from . import views 

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('details/<int:pk>/', views.blog_contents, name='blog_contents'),
    
    # blogs
    path('all/', views.blog_all, name='blog_all'),
    path('form/', views.blog_form, name='blog_form'),
    path('update/<int:pk>/', views.blog_form, name='blog_update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    
    # blog_content 
    path('contents/', views.blog_content_all, name='blog_content_all'),
    path('content/form/', views.blog_content_form, name='blog_content_form'),
    path('content/update/<int:pk>/', views.blog_content_form, name='blog_content_update'),
    path('content/delete/<int:pk>/', views.blog_content_delete, name='blog_content_delete'),
    
    # subscribe urls
    path('subscribes/', views.subscribe_all, name='subscribe_all'),
]
