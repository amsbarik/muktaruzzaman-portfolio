from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from .pdfkit_settings import generate_pdf_from_html

from apps.users.views import is_superuser

from .models import Resume, ResumeExperience, ResumeExperienceKey, ResumeProject, ResumeProjectTechnology, TechnicalSkill, ProfessionalSkill, ResumeEducation, ResumeAward, ResumeLanguage, ResumeInterest

from .forms import ResumeForm, ResumeExperienceForm, ResumeExperienceKeyForm, ResumeProjectForm, ResumeProjectTechnologyForm, TechnicalSkillForm, ProfessionalSkillForm, ResumeEducationForm, ResumeAwardForm, ResumeLanguageForm, ResumeInterestForm



# Create your views here.
def resume_online(request):
    resume = Resume.objects.first()
    
    resume_experiences = resume.resume_experience.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_projects = resume.resume_project.filter(is_active=True).order_by('order', 'created_at')[:2]
    
    technical_skills = resume.resume_technical_skill.filter(is_active=True).order_by('order', 'created_at').all()
    professional_skills = resume.resume_professional_skill.filter(is_active=True).order_by('order', 'created_at').all()
    resume_educations = resume.resume_education.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_awards = resume.resume_award.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_languages = resume.resume_language.filter(is_active=True).order_by('order', 'created_at').all()
    resume_interests = resume.resume_interest.filter(is_active=True).order_by('order', 'created_at').all()
    
    context = {
        'resume' : resume,
        'resume_experiences' : resume_experiences,
        'resume_projects' : resume_projects,
        
        'technical_skills' : technical_skills,
        'professional_skills' : professional_skills,
        'resume_educations' : resume_educations,
        'resume_awards' : resume_awards,
        'resume_languages' : resume_languages,
        'resume_interests' : resume_interests,
    }
    
    return render(request, 'resume/resume_online.html', context)


# resume pdf view 
def resume_pdf(request):
    resume = Resume.objects.first()
    
    resume_experiences = resume.resume_experience.filter(is_active=True).order_by('order', 'created_at')[:2]
    # experience = get_object_or_404(resume_experiences)
    # resume_experience_keys = experience.resume_experience_key.all()
    
    resume_projects = resume.resume_project.filter(is_active=True).order_by('order', 'created_at')[:2]
        
    # project = get_object_or_404(resume_projects)
    
    # project_technologies = project.resume_project_technology.all()
    
    technical_skills = resume.resume_technical_skill.filter(is_active=True).order_by('order', 'created_at').all()
    professional_skills = resume.resume_professional_skill.filter(is_active=True).order_by('order', 'created_at').all()
    resume_educations = resume.resume_education.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_awards = resume.resume_award.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_languages = resume.resume_language.filter(is_active=True).order_by('order', 'created_at').all()
    resume_interests = resume.resume_interest.filter(is_active=True).order_by('order', 'created_at').all()
    
    context = {
        'resume' : resume,
        'resume_experiences' : resume_experiences,
        # 'resume_experience_keys' : resume_experience_keys,
        
        'resume_projects' : resume_projects,
        # 'project_technologies' : project_technologies,
        
        'technical_skills' : technical_skills,
        'professional_skills' : professional_skills,
        'resume_educations' : resume_educations,
        'resume_awards' : resume_awards,
        'resume_languages' : resume_languages,
        'resume_interests' : resume_interests,
        'context' : 'data',
    }
    
    # Render the HTML template with context
    html_string = render_to_string('resume/resume_pdf.html', context)
    
    # Convert HTML to PDF
    pdf = generate_pdf_from_html(html_string)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="abdul-barik-resume.pdf"'
    return response







# my pdf view 
# def resume_pdf(request):
#     # Assuming resume template
#     html_string = render_to_string('resume/resume_pdf.html', {'context': 'data'})
    
#     # Convert HTML to PDF
#     pdf = generate_pdf_from_html(html_string)
    
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="abdul-barik-resume.pdf"'
#     return response


# from .pdf import html2pdf
# def resume_pdf(request):
#     pdf = html2pdf('resume/resume_pdf.html')
#     return HttpResponse(pdf, content_type='application/pdf')







# try to generate pdf file 
# from django.http import FileResponse 
# import io 
# from reportlab.pdfgen import canvas 
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter 


# def venue_pdf(request):
#     # create Bytestream buffer 
#     buf = io.BytesIO()
#     # create canvas 
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # create text object 
#     textob = c.beginPath()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont('Montserat', 14)
    
    
#     # add some line of text 
#     lines = [
#         'This is line 1',
#         'This is line 2',
#         'This is line 3',
#     ]
    
#     # loop 
#     for line in lines:
#         textob.textLine(line)
        
        
#     # finish up 
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
    
#     return FileResponse(buf, as_attachment=True, filename='venue.pdf')
    
    
    
    
    
    
    
    
    
    
# ////////////////////// admin resume view start here /////////////////////////
@login_required
@user_passes_test(is_superuser)
def resume(request):
    # resume = Resume.objects.all()
    
    resume = Resume.objects.first()
    
    resume_experiences = resume.resume_experience.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_projects = resume.resume_project.filter(is_active=True).order_by('order', 'created_at')[:2]
    
    technical_skills = resume.resume_technical_skill.filter(is_active=True).order_by('order', 'created_at').all()
    professional_skills = resume.resume_professional_skill.filter(is_active=True).order_by('order', 'created_at').all()
    resume_educations = resume.resume_education.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_awards = resume.resume_award.filter(is_active=True).order_by('order', 'created_at')[:2]
    resume_languages = resume.resume_language.filter(is_active=True).order_by('order', 'created_at').all()
    resume_interests = resume.resume_interest.filter(is_active=True).order_by('order', 'created_at').all()
    
    context = {
        'resume' : resume,
        'resume_experiences' : resume_experiences,
        'resume_projects' : resume_projects,
        
        'technical_skills' : technical_skills,
        'professional_skills' : professional_skills,
        'resume_educations' : resume_educations,
        'resume_awards' : resume_awards,
        'resume_languages' : resume_languages,
        'resume_interests' : resume_interests,
    }

    return render(request, 'admin_panel/resume/resume.html', context)













@login_required
@user_passes_test(is_superuser)
def resume_form(request, pk=0):

    if request.method == "GET":
        if pk == 0:
            form = ResumeForm()
        else:
            resume = Resume.objects.get(id=pk)
            form = ResumeForm(instance=resume)

        return render(request, 'admin_panel/resume/resume_form.html', {'form': form})
        
    else:

        if pk == 0:
            form = ResumeForm(request.POST, request.FILES)
        else:
            resume = Resume.objects.get(id=pk)
            form = ResumeForm(request.POST, request.FILES, instance=resume)

        if form.is_valid():
            form.save()

        return redirect('admin_resume')
        

# resume experience view 
@login_required
@user_passes_test(is_superuser)
def resume_experience_all(request):
    resume_experiences = ResumeExperience.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/resume_experience_all.html', {'resume_experiences': resume_experiences})


# resume experience create & update 
@login_required
@user_passes_test(is_superuser)
def resume_experience_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeExperienceForm()
        else:
            experience = ResumeExperience.objects.get(id=pk)
            form = ResumeExperienceForm(instance=experience)
    
        return render(request, 'admin_panel/resume/resume_experience_form.html', {'form': form})
        
    else:
        if pk == 0:
            form = ResumeExperienceForm(request.POST)
        else:
            experience = ResumeExperience.objects.get(id=pk)
            form = ResumeExperienceForm(request.POST, instance=experience)
        
        if form.is_valid:
            form.save()
            
        return redirect('resume_experience_all')


# resume_experience_delete
@login_required
@user_passes_test(is_superuser)
def resume_experience_delete(request, pk):
    experience = ResumeExperience.objects.get(id=pk)
    experience.delete()
    return redirect('resume_experience_all')


# resume_experience_keys all 
@login_required
@user_passes_test(is_superuser)
def resume_experience_keys(request):
    keys = ResumeExperienceKey.objects.all()
    return render(request, 'admin_panel/resume/resume_experience_keys.html', {'experience_keys': keys})


# resume experience keys create and update
@login_required
@user_passes_test(is_superuser)
def experience_keys_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeExperienceKeyForm()
        else:
            experience_key = ResumeExperienceKey.objects.get(id=pk)
            form = ResumeExperienceKeyForm(instance=experience_key)
        
        return render(request, 'admin_panel/resume/experience_keys_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeExperienceKeyForm(request.POST)
        else:
            experience_key = ResumeExperienceKey.objects.get(id=pk)
            form = ResumeExperienceKeyForm(request.POST, instance=experience_key)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_experience_keys')


# resume_experience_key_delete
@login_required
@user_passes_test(is_superuser)
def experience_keys_delete(request, pk):
    experience_key = ResumeExperienceKey.objects.get(id=pk)
    experience_key.delete()
    return redirect('resume_experience_keys')


# resume project all view
@login_required
@user_passes_test(is_superuser)
def resume_project_all(request):
    resume_projects = ResumeProject.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/resume/resume_project_all.html', {'resume_projects': resume_projects})


# resume_project_ create & update 
@login_required
@user_passes_test(is_superuser)
def resume_project_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeProjectForm()
        else:
            resume_project = ResumeProject.objects.get(id=pk)
            form = ResumeProjectForm(instance=resume_project)
            
        return render(request, 'admin_panel/resume/resume_project_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeProjectForm(request.POST)
        else:
            resume_project = ResumeProject.objects.get(id=pk)
            form = ResumeProjectForm(request.POST, instance=resume_project)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_project_all')


# resume_project_delete 
@login_required
@user_passes_test(is_superuser)
def resume_project_delete(request, pk):
    resume_project = ResumeProject.objects.get(id=pk)
    resume_project.delete()
    return redirect('resume_project_all')


# Resume Project Technology views
@login_required
@user_passes_test(is_superuser)
def resume_project_technologies(request):
    project_technologies = ResumeProjectTechnology.objects.all()
    return render(request, 'admin_panel/resume/resume_project_technologies.html', {'project_technologies': project_technologies})


# project_technology_form create & update 
@login_required
@user_passes_test(is_superuser)
def project_technology_form(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            form = ResumeProjectTechnologyForm()
        else:
            project_technology = ResumeProjectTechnology.objects.get(id=pk)
            form = ResumeProjectTechnologyForm(instance=project_technology)
            
        return render(request, 'admin_panel/resume/project_technology_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeProjectTechnologyForm(request.POST)
        else:
            project_technology = ResumeProjectTechnology.objects.get(id=pk)
            form = ResumeProjectTechnologyForm(request.POST, instance=project_technology)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_project_technologies')
            

# project_technology_delete
@login_required
@user_passes_test(is_superuser)
def project_technology_delete(requets, pk):
    project_technology = ResumeProjectTechnology.objects.get(id=pk)
    project_technology.delete()
    return redirect('resume_project_technologies')



# Technical Skill view
@login_required
@user_passes_test(is_superuser)
def technical_skill_all(request):
    technical_skills = TechnicalSkill.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/technical_skill_all.html', {'technical_skills': technical_skills})


#technical skill form create & update
@login_required
@user_passes_test(is_superuser)
def technical_skill_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0 :
            form = TechnicalSkillForm()
        else:
            technical_skill = TechnicalSkill.objects.get(id=pk)
            form = TechnicalSkillForm(instance=technical_skill)
            
        return render(request, 'admin_panel/resume/technical_skill_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = TechnicalSkillForm(request.POST)
        else:
            technical_skill = TechnicalSkill.objects.get(id=pk)
            form = TechnicalSkillForm(request.POST, instance=technical_skill)
            
        if form.is_valid:
            form.save()
            
        return redirect('technical_skill_all')
    
    
#technical skill delete
@login_required
@user_passes_test(is_superuser)
def technical_skill_delete(request, pk):
    technical_skill = TechnicalSkill.objects.get(id=pk)
    technical_skill.delete()
    return redirect('technical_skill_all')
    
# professional Skill view
@login_required
@user_passes_test(is_superuser)
def professional_skill_all(request):
    professional_skills = ProfessionalSkill.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/professional_skill_all.html', {'professional_skills': professional_skills})


#professional skill form create & update
@login_required
@user_passes_test(is_superuser)
def professional_skill_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0 :
            form = ProfessionalSkillForm()
        else:
            professional_skill = ProfessionalSkill.objects.get(id=pk)
            form = ProfessionalSkillForm(instance=professional_skill)
            
        return render(request, 'admin_panel/resume/professional_skill_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ProfessionalSkillForm(request.POST)
        else:
            professional_skill = ProfessionalSkill.objects.get(id=pk)
            form = ProfessionalSkillForm(request.POST, instance=professional_skill)
            
        if form.is_valid:
            form.save()
            
        return redirect('professional_skill_all')
    
    
#professional skill delete
@login_required
@user_passes_test(is_superuser)
def professional_skill_delete(request, pk):
    professional_skill = ProfessionalSkill.objects.get(id=pk)
    professional_skill.delete()
    return redirect('professional_skill_all')



# resume education view
@login_required
@user_passes_test(is_superuser)
def resume_education_all(request):
    resume_educations = ResumeEducation.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/resume_education_all.html', {'resume_educations': resume_educations})


#resume education form create & update
@login_required
@user_passes_test(is_superuser)
def resume_education_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeEducationForm()
        else:
            resume_education = ResumeEducation.objects.get(id=pk)
            form = ResumeEducationForm(instance=resume_education)
            
        return render(request, 'admin_panel/resume/resume_education_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeEducationForm(request.POST)
        else:
            resume_education = ResumeEducation.objects.get(id=pk)
            form = ResumeEducationForm(request.POST, instance=resume_education)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_education_all')
    
    
#resume education delete
@login_required
@user_passes_test(is_superuser)
def resume_education_delete(request, pk):
    resume_education = ResumeEducation.objects.get(id=pk)
    resume_education.delete()
    return redirect('resume_education_all')
    


# resume award view
@login_required
@user_passes_test(is_superuser)
def resume_award_all(request):
    resume_awards = ResumeAward.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/resume_award_all.html', {'resume_awards': resume_awards})


#resume award form create & update
@login_required
@user_passes_test(is_superuser)
def resume_award_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeAwardForm()
        else:
            resume_award = ResumeAward.objects.get(id=pk)
            form = ResumeAwardForm(instance=resume_award)
            
        return render(request, 'admin_panel/resume/resume_award_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeAwardForm(request.POST)
        else:
            resume_award = ResumeAward.objects.get(id=pk)
            form = ResumeAwardForm(request.POST, instance=resume_award)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_award_all')
    
    
#resume award delete
@login_required
@user_passes_test(is_superuser)
def resume_award_delete(request, pk):
    resume_award = ResumeAward.objects.get(id=pk)
    resume_award.delete()
    return redirect('resume_award_all')
    


# resume language view
@login_required
@user_passes_test(is_superuser)
def resume_language_all(request):
    resume_languages = ResumeLanguage.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/resume_language_all.html', {'resume_languages': resume_languages})


#resume language form create & update
@login_required
@user_passes_test(is_superuser)
def resume_language_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeLanguageForm()
        else:
            resume_language = ResumeLanguage.objects.get(id=pk)
            form = ResumeLanguageForm(instance=resume_language)
            
        return render(request, 'admin_panel/resume/resume_language_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeLanguageForm(request.POST)
        else:
            resume_language = ResumeLanguage.objects.get(id=pk)
            form = ResumeLanguageForm(request.POST, instance=resume_language)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_language_all')
    
    
#resume language delete
@login_required
@user_passes_test(is_superuser)
def resume_language_delete(request, pk):
    resume_language = ResumeLanguage.objects.get(id=pk)
    resume_language.delete()
    return redirect('resume_language_all')
    


# resume language view
@login_required
@user_passes_test(is_superuser)
def resume_interest_all(request):
    resume_interests = ResumeInterest.objects.order_by('created_at').all()
    return render(request, 'admin_panel/resume/resume_interest_all.html', {'resume_interests': resume_interests})


#resume language form create & update
@login_required
@user_passes_test(is_superuser)
def resume_interest_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = ResumeInterestForm()
        else:
            resume_interest = ResumeInterest.objects.get(id=pk)
            form = ResumeInterestForm(instance=resume_interest)
            
        return render(request, 'admin_panel/resume/resume_interest_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = ResumeInterestForm(request.POST)
        else:
            resume_interest = ResumeInterest.objects.get(id=pk)
            form = ResumeInterestForm(request.POST, instance=resume_interest)
            
        if form.is_valid:
            form.save()
            
        return redirect('resume_interest_all')
    
    
#resume language delete
@login_required
@user_passes_test(is_superuser)
def resume_interest_delete(request, pk):
    resume_interest = ResumeInterest.objects.get(id=pk)
    resume_interest.delete()
    return redirect('resume_interest_all')
    













   
    
    
    
    
    