from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile,name = 'profile'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('profile/posts/', views.view_my_posts,name = 'view_my_posts'),
    path('members/', views.view_members,name = 'view_members'),
    path('activity/', views.view_activity,name = 'view_activity'),
    path('register_user/', views.register_user,name = 'register_user'),
    path('authenticate_pending_users/', views.authenticate_pending_users,name = 'authenticate_pending_users'),
]