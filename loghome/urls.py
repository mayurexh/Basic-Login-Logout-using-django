from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/',views.aboutus_view, name="about"),
    path('register/', views.register_view, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='loghome/login.html'), name="login" ),
    path('logout/',auth_views.LogoutView.as_view(), name="logout")

]