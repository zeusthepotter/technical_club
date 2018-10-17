from django import forms
from django.contrib.auth.models import User
from .models import Post, Member

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


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