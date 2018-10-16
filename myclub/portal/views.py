from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from .forms import PostForm, UserForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



def index(request):
    return HttpResponse("Hello, world. You're at the portal's homepage.")

@login_required
def profile(request):
    # roll = Member.objects.get(name=n).roll
    # s='lolol'+ n + str(roll)
    # return HttpResponse(s)
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
    members = Member.objects.all()
    return render(request, 'portal/members.html', {'user':request.user ,'members':members })

@login_required
def view_activity(request):
    posts = Post.objects.order_by("-published_date")
    return render(request, 'portal/activity.html', {'posts':posts})



def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            #Pending_User.objects.create(roll = form.cleaned_data['roll'], password = form.cleaned_data['password'], email = form.cleaned_data['email'], contact_no = form.cleaned_data['contact_no'], branch = form.cleaned_data['branch'], year = form.cleaned_data['year'], profile_picture=request.FILES['profile_picture'], role = form.cleaned_data['role'], team = form.cleaned_data['team'])
            # redirect, or however you want to get to the main view
            
            p = form.save()
            
            return HttpResponseRedirect('/portal/members') 

        
    form = UserForm() 
    return render(request, 'portal/register_user.html', {'form': form})

@login_required    
def authenticate_pending_users(request):
    
    P = Member.objects.filter(pending_status=True)
    if request.method == "POST":
        m= Member.objects.get(pk=request.POST.get('choice'))
        m.pending_status=False
        m.save()
    
    return render(request, 'portal/authenticate_pending_users.html',{ 'P': P } )