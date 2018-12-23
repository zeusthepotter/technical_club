from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from .forms import PostForm, UserForm, ProjectForm, AnnouncementForm
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mass_mail, send_mail
from django.views.generic.edit import UpdateView



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('password_reset_successful')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'portal/change_password.html', {
        'form': form
    })

@login_required
def password_reset_successful(request):
        
    
    return render(request, 'portal/password_reset_success.html')



@login_required
def profile(request):
    
    
    
    return render(request, 'portal/profile.html', context = {'member': request.user.member, 'posts': Post.objects.filter(author=request.user) } )

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('profile')
    else:
        form = PostForm(request.user)
    
    return render(request, 'portal/add_post.html', context = {'member': request.user.member, 'form':form } )

@login_required
def make_announcement(request):
    if request.method == "POST":
        form = AnnouncementForm(request.user, request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.published_date = timezone.now()
            announcement.save()
            if form.cleaned_data['recipients']=='Admins':
                email_recipients = [str(m.email) for m in Member.objects.all() if m.user.is_superuser]

            if form.cleaned_data['recipients']=='Assistant Coordinators':
                email_recipients = [str(m.email) for m in Member.objects.all() if m.user.member.role=='Assistant Coordinator']

            if form.cleaned_data['recipients']=='All Members':
                email_recipients = [str(m.email) for m in Member.objects.all()]

            

            message = ('Technical Club RECK - ' + announcement.title, announcement.text, 'Technical Club RECK',email_recipients)
            send_mass_mail((message,), fail_silently=True)

            return redirect('view_announcements')
    else:
        form = AnnouncementForm(request.user)
    
    return render(request, 'portal/make_announcement.html', context = {'member': request.user.member, 'form':form } )


@login_required
def create_project(request):
    if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                project = form.save()
                
                return redirect('profile')
    else:
        form = ProjectForm()
        
    return render(request, 'portal/create_project.html', context = {'member': request.user.member, 'form':form } )


# @login_required
# def update_project(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             project = form.save()
#
#             return redirect('view-project')
#     else:
#         form = ProjectForm()
#
#     return render(request, 'portal/update_project.html', context={'member': request.user.member, 'form': form})
# class updateProject(UpdateView):
#     model = Project
#     fields = ['worker','deadline','finished']
#     template_name = 'portal/update_project.html'


@login_required
def view_profile(request,pk):
        
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'portal/view_profile.html', context = {'member': member } )


@login_required
def view_project(request,pk):
        
    p = get_object_or_404(Project, pk=pk)
    return render(request, 'portal/project.html', context = {'p': p } )


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
def view_members(request):
    members = Member.objects.filter(pending_status=False)
    return render(request, 'portal/members.html', {'user':request.user ,'members':members })

@login_required
def view_activity(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'portal/activity.html', {'posts':posts})

@login_required
def view_announcements(request):
    announcements = Announcement.objects.order_by("-published_date")
    return render(request, 'portal/announcements.html', {'announcements':announcements})


@login_required
def view_my_activity(request):
    posts = Post.objects.filter(author=request.user).order_by("-published_date")
    return render(request, 'portal/my_activity.html', {'posts':posts})



@login_required
def view_projects(request):
    p = Project.objects.order_by("deadline")
    return render(request, 'portal/projects.html', {'projects':p})



@login_required
def view_my_projects(request):
    p = Project.objects.filter(worker=request.user).order_by("deadline")
    return render(request, 'portal/my_projects.html', {'projects':p})



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
            email_recipients = [str(m.email) for m in Member.objects.all() if m.user.is_superuser]
            message = ('Technical Club RECK - ', p.name + ' just registered on the portal.',  'Technical Club RECK',email_recipients)
            send_mass_mail((message,), fail_silently=True)

            return HttpResponseRedirect('/portal/reg_successful') 

    else:

        form = UserForm()
        
        
    
    return render(request, 'portal/register_user.html', {'form': form})



def reg_successful(request):
        

    return render(request, 'portal/reg_successful.html' )

def chat(request):
    return render(request, 'portal/chat.html' )

@login_required    
def authenticate_pending_users(request):
    
    P = Member.objects.filter(pending_status=True)
    if request.method == "POST":
        m= Member.objects.get(pk=request.POST.get('choice'))
        m.pending_status=False
        m.save()
        send_mail('Technical Club RECK', 'Your account on the portal has been authenticated.', 'Technical Club RECK', [str(m.email)], fail_silently=False,)
    
    return render(request, 'portal/authenticate_pending_users.html',{ 'P': P } )