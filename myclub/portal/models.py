from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30,null = True,blank=True)
    contact_no = models.CharField(max_length=10)
    email=models.EmailField(max_length=70)
    branch = models.CharField(max_length=30, choices = ( ('CSE','CSE'), ('Civil','Civil'), ('Electronics','Electronics'), ('Electrical','Electrical')  )    ,null = True,blank=True)
    year = models.CharField(max_length=30, choices = ( ('First Year','First Year'), ('Second Year','Second Year'), ('Third Year','Third Year'), ('Fourth Year','Fourth Year')  ) ,null = True,blank=True)
    profile_picture = models.ImageField(blank=True, null=True)
    role = models.CharField(max_length=30, choices = ( ('Volunteer','Volunteer'), ('Coordinator','Coordinator') ) ,null = True,blank=True)
    team = models.CharField(max_length=30, choices = ( ('Technical Team','Technical Team'), ('Documentation Team','Documentation Team'), ('Design Team','Design Team'), ('Sponsorship Team','Sponsorship Team')  ) ,null = True,blank=True)
    pending_status = models.BooleanField(default=True)

    @property
    def image_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return "/static/portal/robot.jpg"


    def __str__(self):
        return self.name + ' ' + str(self.roll)


class Project(models.Model):
    worker = models.ManyToManyField(User)
    title =  models.CharField(max_length=100)
    description =  models.CharField(max_length=500)
    deadline = models.DateField()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.OneToOneField(Project,on_delete=models.CASCADE,null = True,blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

