from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name= 'cities_index'),
    path('accounts/posts_show/', views.posts_show, name= 'posts_show'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile')
]
