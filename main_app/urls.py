from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/edit_profile', views.edit_profile, name='edit_profile'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name= 'cities_index'),
    path('posts_show/<int:post_id>/', views.posts_show, name= 'posts_show'),
    path('cities/<int:city_id>/', views.cities_show, name= 'cities_show'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('posts_new/', views.make_post, name='posts_new'),
    path('posts_edit/<int:post_id>/', views.edit_post, name='posts_edit'),
    path('posts_delete/<int:post_id>/', views.posts_delete, name='posts_delete'),
]
