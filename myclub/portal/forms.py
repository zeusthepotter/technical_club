from django import forms
from django.contrib.auth.models import User
from .models import Post, Member

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('roll', 'name', 'password', 'email','contact_no','branch','year','profile_picture','role','team')  