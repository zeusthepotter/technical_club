from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile,name = 'profile'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile'),
    path('update_project/<int:pk>/', views.updateProject.as_view() , name='update_project'),
    path('project/<int:pk>/', views.view_project, name='view_project'),
    path('profile/posts/', views.view_my_posts,name = 'view_my_posts'),
    path('add_post/', views.add_post,name = 'add_post'),
    path('make_announcement/', views.make_announcement,name = 'make_announcement'),
    path('members/', views.view_members,name = 'view_members'),
    path('activity/', views.view_activity,name = 'view_activity'),
    path('announcements/', views.view_announcements,name = 'view_announcements'),
    path('my_activity/', views.view_my_activity,name = 'view_my_activity'),
    path('register_user/', views.register_user,name = 'register_user'),
    path('authenticate_pending_users/', views.authenticate_pending_users,name = 'authenticate_pending_users'),
    path('reg_successful/', views.reg_successful,name = 'reg_successful'),
    path('projects/', views.view_projects,name = 'view_projects'),
    path('my_projects/', views.view_my_projects,name = 'view_my_projects'),
    path('create_project/', views.create_project,name = 'create_project'),
    path('chat/', views.chat,name = 'chat'),
    path('change_password/', views.change_password,name = 'change_password'),
    path('password_reset_successful/', views.password_reset_successful,name = 'password_reset_successful'),
]