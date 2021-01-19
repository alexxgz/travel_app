from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    # path('accounts/profile/edit', views.profile_edit, name='profile_edit'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name= 'cities_index'),
    path('posts_show/', views.posts_show, name= 'posts_show'),
    path('cities_show/', views.cities_show, name= 'cities_show'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/user_edit', views.edit_profile, name='profile'),
]
