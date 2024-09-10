from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from apps.users.views import is_superuser
from apps.users.models import UserSetting

from .forms import ProjectForm, TestimonialForm, FeedbackForm, ProjectCaseStudyForm, ProjectDeveloperForm, ProjectStatusForm, ProjectTechnologyForm, ProjectRequirmentForm, ProjectResultForm
from .models import Project, ProjectCaseStudy, ProjectTechnology, ProjectRequirment, ProjectResult, Testimonial, ProjectDeveloper

# user import 
from apps.users.models import Team, Gender, Role
from apps.users.forms import TeamForm



# # Create your views here.
def portfolio(request):
    projects = Project.objects.filter(is_active=True).order_by('order', 'created_at').all()
    return render(request, 'portfolio/portfolio.html', {'projects' : projects})

def case_study(request, pk):
    project = get_object_or_404(Project, id=pk)
    case_study = project.case_study  # This will automatically fetch the related case study
    technologies = case_study.technologies.all()
    requirments = case_study.requirments.all()
    results = case_study.results.all()
    testimonial = project.testimonials.filter(is_active=True).order_by('order', 'created_at').first()
    
    context = {
        'project' : project,
        'case_study' : case_study, 
        'technologies' : technologies,
        'requirments': requirments,
        'results' : results,
        'testimonial': testimonial,
    }
    
    return render(request, 'portfolio/case_study.html', context)


# feedback view 
def feedback(request):
    
    projects = Project.objects.all()
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks a lot for your valuable feedback')
            return redirect('feedback')
    else:
        form = FeedbackForm()
        
    context = {
        'projects': projects,
        'form': form,
    }
        
    return render(request, 'portfolio/feedback.html', context)
    
    
    
    
    
    

#//////////// projects admin views start here //////////////////////////

# project show all view
@login_required
@user_passes_test(is_superuser)
def project_all(request):
    
    status = request.GET.get('status')
    
    if status:
        projects = Project.objects.filter(status=status).order_by('created_at')
    else:
        projects = Project.objects.order_by('created_at').all()
    
    context = {
        'projects': projects,
        'status': status,
    }
    
    return render(request, 'admin_panel/portfolio/project_all.html', context)


# project add and update form view 
@login_required
@user_passes_test(is_superuser)
def project_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProjectForm()
        else:
            project = Project.objects.get(id=pk)
            form = ProjectForm(instance=project)
            
        return render(request, 'admin_panel/portfolio/project_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ProjectForm(request.POST, request.FILES)
            
        else:
            project = Project.objects.get(id=pk)
            form = ProjectForm(request.POST, request.FILES, instance=project)
            
        if form.is_valid():
            form.save()
            return redirect('project_all')



# projects_by_status
@login_required
@user_passes_test(is_superuser)
def projects_by_status(request, status):
    projects = Project.objects.filter(status=status)
    return render(request, 'admin_panel/portfolio/project_all.html', {'projects': projects, 'status': status})



# project developers (view) view 
@login_required
@user_passes_test(is_superuser)
def project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    developers = project.project_name.all()
    case_study = project.case_study
    technologies = case_study.technologies.all()
    requirments = case_study.requirments.all()
    # results = case_study.results.all()
    testimonial = project.testimonials.filter(is_active=True).order_by('order', 'created_at').first()
    
    # status update 
    if request.method == 'POST':
        form = ProjectStatusForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project status updated successfully.')
            return redirect('project_view', project_id=project.id)
            # return redirect('project_all')
        
    else:
        form = ProjectStatusForm(instance=project)
        
    
    context = {
        'project': project,
        'developers': developers,
        'form': form,
        'case_study': case_study,
        'technologies': technologies,
        'requirments':requirments,
        'testimonial': testimonial,
    }
    
    return render(request, 'admin_panel/portfolio/project_view.html', context)



# def update_project_status(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     if request.method == 'POST':
#         form = ProjectStatusForm(request.POST, instance=project)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Project status updated successfully.')
#             return redirect('project_detail', project_id=project.id)
#     else:
#         form = ProjectStatusForm(instance=project)
#     return render(request, 'projects/update_status.html', {'form': form, 'project': project})



# this view pre-select the project & more project available
# def developer_assign(request, project_id=None):
#     # pre select the project 
#     if project_id:
#         project = Project.objects.get(id=project_id)
#         form = ProjectDeveloperForm(initial={'project': project})
#     else:
#         form = ProjectDeveloperForm()
    
#     # save the assign form 
#     if request.method == 'POST':
#         form = ProjectDeveloperForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('project_all')
#         else:
#             form = ProjectDeveloperForm()
            
#     return render(request, 'admin_panel/portfolio/developer_assign.html', {'form': form})


# this view pre-select the project & other project not available
@login_required
@user_passes_test(is_superuser)
def developer_assign(request, project_id=None, dev_id=None):
    
    if request.method == 'POST':
        if project_id:
            form = ProjectDeveloperForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('project_all')
            
        elif project_id and dev_id:
            project = get_object_or_404(Project, id=project_id)
            developer = ProjectDeveloper.objects.get(id=dev_id)
            form = ProjectDeveloperForm(request.POST, instance=developer)
            
            if form.is_valid():
                form.save()
                
                return redirect('project_view', project_id=project.id) #not work
                # return redirect('project_all')  #work
    else:
        if project_id:
            project = Project.objects.get(id=project_id)
            form = ProjectDeveloperForm(initial={'project': project})
            form.fields['project'].queryset = Project.objects.filter(id=project_id)
            
        elif dev_id:
            developer = ProjectDeveloper.objects.get(id=dev_id)
            form = ProjectDeveloperForm( instance=developer)
            
        else:
            form = ProjectDeveloperForm()

    return render(request, 'admin_panel/portfolio/developer_assign.html', {'form': form})









#project delete
@login_required
@user_passes_test(is_superuser)
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('project_all')


## Project Case Study views start ////////////////
@login_required
@user_passes_test(is_superuser)
def project_case_study_all(request):
    project_case_studies = ProjectCaseStudy.objects.all()
    return render(request, 'admin_panel/portfolio/project_case_study_all.html', {'project_case_studies': project_case_studies})



@login_required
@user_passes_test(is_superuser)
def project_case_study_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProjectCaseStudyForm()
        else:
            case_study = ProjectCaseStudy.objects.get(id=pk)
            form = ProjectCaseStudyForm(instance=case_study)
        
        return render(request, 'admin_panel/portfolio/project_case_study_form.html', {'form': form})
            
    else:
        if pk == 0:
            form = ProjectCaseStudyForm(request.POST, request.FILES)
        else:
            case_study = ProjectCaseStudy.objects.get(id=pk)
            form = ProjectCaseStudyForm(request.POST, request.FILES, instance=case_study)
            
        if form.is_valid():
            form.save()
        
        return redirect('project_case_study_all')
    
    
# Project Technology views
@login_required
@user_passes_test(is_superuser)
def project_technology_all(request):
    project_technologies = ProjectTechnology.objects.all()
    return render(request, 'admin_panel/portfolio/project_technology_all.html', {'project_technologies': project_technologies})


@login_required
@user_passes_test(is_superuser)
def project_technology_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProjectTechnologyForm()
        else:
            project_technology = ProjectTechnology.objects.get(id=pk)
            form = ProjectTechnologyForm(instance=project_technology)
        
        return render(request, 'admin_panel/portfolio/project_technology_form.html', {'form': form})
            
    else:
        if pk == 0:
            form = ProjectTechnologyForm(request.POST)
        else:
            project_technology = ProjectTechnology.objects.get(id=pk)
            form = ProjectTechnologyForm(request.POST, instance=project_technology)
            
        if form.is_valid():
            form.save()
        
        return redirect('projects_technology_all')
    
    
@login_required
@user_passes_test(is_superuser)
def project_technology_delete(request, pk):
    project_technology = ProjectTechnology.objects.get(id=pk)
    project_technology.delete()
    return redirect('projects_technology_all')
    
    
# Project Requirment views
@login_required
@user_passes_test(is_superuser)
def project_requirment_all(request):
    project_requirments = ProjectRequirment.objects.all()
    return render(request, 'admin_panel/portfolio/project_requirment_all.html', {'project_requirments': project_requirments})



@login_required
@user_passes_test(is_superuser)
def project_requirment_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProjectRequirmentForm()
        else:
            project_requirment = ProjectRequirment.objects.get(id=pk)
            form = ProjectRequirmentForm(instance=project_requirment)
        
        return render(request, 'admin_panel/portfolio/project_requirment_form.html', {'form': form})
            
    else:
        if pk == 0:
            form = ProjectRequirmentForm(request.POST)
        else:
            project_requirment = ProjectRequirment.objects.get(id=pk)
            form = ProjectRequirmentForm(request.POST, instance=project_requirment)
            
        if form.is_valid():
            form.save()
        
        return redirect('project_requirment_all')
    
    
@login_required
@user_passes_test(is_superuser)
def project_requirment_delete(request, pk):
    project_requirment = ProjectRequirment.objects.get(id=pk)
    project_requirment.delete()
    return redirect('project_requirment_all')
    
    
    
# Project Results views
@login_required
@user_passes_test(is_superuser)
def project_result_all(request):
    project_results = ProjectResult.objects.all()
    return render(request, 'admin_panel/portfolio/project_result_all.html', {'project_results': project_results})



@login_required
@user_passes_test(is_superuser)
def project_result_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ProjectResultForm()
        else:
            project_result = ProjectResult.objects.get(id=pk)
            form = ProjectResultForm(instance=project_result)
        
        return render(request, 'admin_panel/portfolio/project_result_form.html', {'form': form})
            
    else:
        if pk == 0:
            form = ProjectResultForm(request.POST)
        else:
            project_result = ProjectResult.objects.get(id=pk)
            form = ProjectResultForm(request.POST, instance=project_result)
            
        if form.is_valid():
            form.save()
        
        return redirect('project_result_all')
    
    
@login_required
@user_passes_test(is_superuser)
def project_result_delete(request, pk):
    project_result = ProjectResult.objects.get(id=pk)
    project_result.delete()
    return redirect('project_result_all')
    
    
    



# users view here start /////////////////////////
# @login_required
# @user_passes_test
@login_required
@user_passes_test(is_superuser)
def developer_all(request):
    team = Team.objects.all()
    return render(request, 'admin_panel/users/developer_all.html', {'team' : team})


@login_required
@user_passes_test(is_superuser)
def developer_add(request):
    form = TeamForm()
    
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, 'Developer successfully added!')
            return redirect('developer_all')
        else:
            # form = TeamForm()
            messages.error(request, 'There was an error adding the developer. Please check the form and try again.')
        
    return render(request, 'admin_panel/users/developer_add.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def developer_update(request, pk):
    developer = Team.objects.get(id=pk)
    form = TeamForm(instance=developer)
    
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=developer)
        if form.is_valid:
            form.save()
            messages.success(request, 'This developer updated successfully!')
            return redirect('developer_all')
            
        else:
            form = TeamForm(instance=developer)
            
    return render(request, 'admin_panel/users/developer_update.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def developer_delete(request, pk):
    developer = Team.objects.get(id=pk)
    developer.delete()
    return redirect('developer_all')




# Testimonial view
@login_required
@user_passes_test(is_superuser)
def testimonial_all(request):
    testimonials = Testimonial.objects.order_by('created_at').all()
    return render(request, 'admin_panel/testimonials/testimonial_all.html', {'testimonials': testimonials})


    
    
# testimonial_form 
@login_required
@user_passes_test(is_superuser)
def testimonial_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = TestimonialForm()
        else:
            testimonial = Testimonial.objects.get(id=pk)
            form = TestimonialForm(instance=testimonial)
        
        return render(request, 'admin_panel/testimonials/testimonial_form.html', {'form': form})
            
    else:
        if pk == 0:
            form = TestimonialForm(request.POST, request.FILES)
        else:
            testimonial = Testimonial.objects.get(id=pk)
            form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
            
        if form.is_valid():
            form.save()
        
        return redirect('testimonial_all')
    

# testimonial_delete
@login_required
@user_passes_test(is_superuser)
def testimonial_delete(request,pk):
    testimonial = Testimonial.objects.get(id=pk)
    testimonial.delete()
    return redirect('testimonial_all')










