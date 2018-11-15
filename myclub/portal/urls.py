from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile,name = 'profile'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile'),
    path('project/<int:pk>/', views.view_project, name='view_project'),
    path('profile/posts/', views.view_my_posts,name = 'view_my_posts'),
    path('add_post/', views.add_post,name = 'add_post'),
    path('members/', views.view_members,name = 'view_members'),
    path('activity/', views.view_activity,name = 'view_activity'),
    path('register_user/', views.register_user,name = 'register_user'),
    path('authenticate_pending_users/', views.authenticate_pending_users,name = 'authenticate_pending_users'),
    path('reg_successful/', views.reg_successful,name = 'reg_successful'),
    path('projects/', views.view_projects,name = 'view_projects'),
    path('my_projects/', views.view_my_projects,name = 'view_my_projects'),
    path('create_project/', views.create_project,name = 'create_project'),
    path('red_zone/', views.view_red_zone,name = 'red_zone'),
    path('chat/', views.chat,name = 'chat'),
]