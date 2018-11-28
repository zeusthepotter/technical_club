from django.contrib import admin
from .models import Member, Post, Project, Announcement


admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(Project)

