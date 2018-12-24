from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post, Member, Project, Announcement
from django_select2.forms import Select2MultipleWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'project')
    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(worker=user)

class AnnouncementForm(forms.ModelForm):

    recipients = forms.ChoiceField(widget=forms.Select() , choices = ( ('All members','All members'), ('Assistant Coordinators','Assistant Coordinators'), ('Admins','Admins')) )


    class Meta:
        model = Announcement
        fields = ('title', 'text','recipients')


    
    def __init__(self, user, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = ('title', 'description','worker','deadline','finished')
        widgets = {
            'worker': Select2MultipleWidget
        }


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('deadline','worker','finished')
        widgets = {
            'worker': Select2MultipleWidget
        }

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
        else:
            if image.size>300*1024:
                raise forms.ValidationError(
                "The size of your profile picture must not exceed 300 KB!"
            )

        
