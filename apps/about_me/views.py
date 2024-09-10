from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from apps.users.views import is_superuser
from apps.portfolio.models import Project

from .models import SkillIcon, Skill
from .forms import SkillIconForm, SkillForm

from apps.portfolio.models import Testimonial
from apps.blogs.models import Blog

# # Create your views here.
def index(request, limit=3):
    
    skills = Skill.objects.filter(is_active=True).order_by('order','created_at')[:8]
    projects = Project.objects.filter(is_active=True).order_by('order','created_at')[:4]
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'created_at')[:limit]
    blogs = Blog.objects.filter(is_active=True).order_by('order', 'created_at')[:limit]
   
    context = { 
    'projects' : projects,
    'skills' : skills,
    'testimonials': testimonials,
    'blogs': blogs,
    }
    
    return render(request, 'about_me/index.html', context)



# admin view start here 

# skill_icon all 
@login_required
@user_passes_test(is_superuser)
def skill_icon_all(request):
    skill_icons = SkillIcon.objects.all()
    
    return render(request, 'admin_panel/about_me/skill_icon_all.html', {'skill_icons': skill_icons})


# skill_icon form 
@login_required
@user_passes_test(is_superuser)
def skill_icon_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = SkillIconForm()
        else:
            skill_icon = get_object_or_404(SkillIcon, id=pk)
            form = SkillIconForm(instance=skill_icon)
        return render(request, 'admin_panel/about_me/skill_icon_form.html', {'form': form})

    else:
        if pk == 0:
            form = SkillIconForm(request.POST)
        else:
            skill_icon = get_object_or_404(SkillIcon, id=pk)
            form = SkillIconForm(request.POST, instance=skill_icon)
        
        if form.is_valid():
            form.save()
            return redirect('skill_icon_all')
        else:
            # If form is not valid, print the errors or display them in the template
            print(form.errors)
            return render(request, 'admin_panel/about_me/skill_icon_form.html', {'form': form})


# skill_icon delete 
@login_required
@user_passes_test(is_superuser)
def skill_icon_delete(request, pk):
    skill_icon = SkillIcon.objects.get(id=pk)
    skill_icon.delete()
    return redirect('skill_icon_all')


# skill view done 
@login_required
@user_passes_test(is_superuser)
def skill_all(request):
    skills = Skill.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/about_me/skill_all.html', {'skills': skills})


# skill_icon form 
@login_required
@user_passes_test(is_superuser)
def skill_form(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = SkillForm()
        else:
            skill = get_object_or_404(Skill, id=pk)
            form = SkillForm(instance=skill)
        return render(request, 'admin_panel/about_me/skill_form.html', {'form': form})

    else:
        if pk == 0:
            form = SkillForm(request.POST, request.FILES)
        else:
            skill = get_object_or_404(Skill, id=pk)
            form = SkillForm(request.POST, request.FILES, instance=skill )
        
        if form.is_valid():
            form.save()
            return redirect('skill_all')
        else:
            # If form is not valid, print the errors or display them in the template
            print(form.errors)
            return render(request, 'admin_panel/about_me/skill_form.html', {'form': form})


# skill_icon delete 
@login_required
@user_passes_test(is_superuser)
def skill_delete(request, pk):
    skill = Skill.objects.get(id=pk)
    skill.delete()
    return redirect('skill_all')




