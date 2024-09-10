from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from .forms import BlogForm, BlogContentForm, SubscribeForm
from .models import Blog, BlogContent, Subscribe
from apps.users.views import is_superuser


# Create your views here.
def blogs(request):
    blogs = Blog.objects.filter(is_active=True).order_by('order', 'created_at').all()
    
    # mail subscribe 
    if request.method == 'POST':
        email = request.POST.get('subsmail')
       
        # validate the data 
        if email:
            Subscribe.objects.create(
                email=email,
            )
            
            messages.success(request, 'Your have subscribed successfully! Thank You')
            return redirect('blogs')
    
    return render(request, 'blogs/blogs.html', {'blogs': blogs})


def blog_contents(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    contents = blog.blog_content
    
    content = {
        'blog' : blog,
        'contents': contents,
    }
    
    return render(request, 'blogs/blog_contents.html', content)



# admin panell blog views here ///////////////////////////////////
@login_required
@user_passes_test(is_superuser)
def blog_all(request):
    blogs = Blog.objects.order_by('created_at').all()
    
    return render(request, 'admin_panel/blogs/blog_all.html', {'blogs': blogs})


# blog create & update form view 
@login_required
@user_passes_test(is_superuser)
def blog_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = BlogForm()
        else:
            blog = Blog.objects.get(id=pk)
            form = BlogForm(instance=blog)
            
        return render(request, 'admin_panel/blogs/blog_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = BlogForm(request.POST, request.FILES)
        else:
            blog = Blog.objects.get(id=pk)
            form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            
        return redirect('blog_all')


# blog delete view 
@login_required
@user_passes_test(is_superuser)
def blog_delete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('blog_all')


# blog content views 
@login_required
@user_passes_test(is_superuser)
def blog_content_all(request):
    blog_contents = BlogContent.objects.all()
    
    return render(request, 'admin_panel/blogs/blog_content_all.html', {'blog_contents': blog_contents})


# blog create & update form view 
@login_required
@user_passes_test(is_superuser)
def blog_content_form(request, pk=0):
    
    if request.method == 'GET':
        if pk == 0:
            form = BlogContentForm()
        else:
            blog_content = BlogContent.objects.get(id=pk)
            form = BlogContentForm(instance=blog_content)
            
        return render(request, 'admin_panel/blogs/blog_content_form.html', {'form': form})
    
    else:
        if pk == 0:
            form = BlogContentForm(request.POST, request.FILES)
        else:
            blog_content = BlogContent.objects.get(id=pk)
            form = BlogContentForm(request.POST, request.FILES, instance=blog_content)

        if form.is_valid():
            form.save()
            
        return redirect('blog_content_all')


# blog delete view 
@login_required
@user_passes_test(is_superuser)
def blog_content_delete(request, pk):
    blog_content = BlogContent.objects.get(id=pk)
    blog_content.delete()
    return redirect('blog_content_all')



# Subscribe view 
@login_required
@user_passes_test(is_superuser)
def subscribe_all(request):
    subscribes = Subscribe.objects.order_by('created_at').all()
    return render(request, 'admin_panel/blogs/subscribe_all.html', {'subscribes': subscribes})







