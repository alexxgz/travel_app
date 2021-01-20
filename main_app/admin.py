from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Post, City
# Register your models here.
UserAdmin.list_display = ('username', 'email', 'is_active', 'date_joined', 'is_staff')
admin.site.register(Profile, UserAdmin) 
admin.site.register(Post)
admin.site.register(City)
