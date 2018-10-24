from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from .forms import PostForm, UserForm, ProjectForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime



def index(request):
    return HttpResponse("Hello, world. You're at the portal's homepage.")

@login_required
def profile(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    
    return render(request, 'portal/profile.html', context = {'member': request.user.member, 'form':form } )


def create_project(request):
    if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                project = form.save()
                
                return redirect('profile')
    else:
        form = ProjectForm()
        
    return render(request, 'portal/create_project.html', context = {'member': request.user.member, 'form':form } )


@login_required
def view_profile(request,pk):
        
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'portal/view_profile.html', context = {'member': member } )


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'portal/post_edit.html', {'form': form, 'post':post })

@login_required
def view_my_posts(request):
    posts= Post.objects.filter(author=request.user)
    return render(request, 'portal/my_posts.html', {'user':request.user ,'posts':posts })


@login_required
def view_red_zone(request):
    u= User.objects.all().filter(project__deadline__lte=datetime.now().date())
    return render(request, 'portal/red_zone.html', {'user':request.user ,'red_users':u })



@login_required
def view_members(request):
    members = Member.objects.filter(pending_status=False)
    return render(request, 'portal/members.html', {'user':request.user ,'members':members })

@login_required
def view_activity(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'portal/activity.html', {'posts':posts})



@login_required
def view_projects(request):
    p = Project.objects.order_by("deadline")
    return render(request, 'portal/projects.html', {'projects':p})



def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            
            user = User.objects.create_user(form.cleaned_data['roll'], form.cleaned_data['email'],form.cleaned_data['password'])
            user.pending_status=False
            user.save()
            p = form.save(commit=False)
            p.user = user
            p.password=''
            p.save()
            
            return HttpResponseRedirect('/portal/reg_successful') 

    else:

        form = UserForm()
        
        
    
    return render(request, 'portal/register_user.html', {'form': form})



def reg_successful(request):
        

    return render(request, 'portal/reg_successful.html' )



@login_required    
def authenticate_pending_users(request):
    
    P = Member.objects.filter(pending_status=True)
    if request.method == "POST":
        m= Member.objects.get(pk=request.POST.get('choice'))
        m.pending_status=False
        m.save()
    
    return render(request, 'portal/authenticate_pending_users.html',{ 'P': P } )