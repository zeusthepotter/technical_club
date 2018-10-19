from django import forms
from django.contrib.auth.models import User
from .models import Post, Member, Project

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ProjectForm(forms.ModelForm):
    deadline=forms.DateTimeField(widget=forms.DateTimeInput())

    class Meta:
        model = Project
        fields = ('title', 'description','worker','deadline')


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ('roll', 'name', 'password', 'confirm_password', 'email','contact_no','branch','year','profile_picture','role','team')  

        

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match the confirm password!"
            )

        image = cleaned_data.get("profile_picture")
        if not image:
            raise forms.ValidationError(
                "Please upload your profile picture!"
            )