"""ninjas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from equipos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipo_edit/', views.equipo_view, name = 'equipo_edit'),
    path('signup/', views.signup_view, name = 'singup_view'),
    path('register/', views.signup_user_view, name = 'register_view'),
    path('login/', auth_views.login, {'template_name': 'equipos/login.html'}, name = 'login'),
    # path('perfil/', views.profile, name = "profile_view"),
    path('index/', views.index, name = "index_view"),
    path('profile/', views.view_profile, name = "index_view"),
    path('logout/', auth_views.logout, {'template_name':'equipos/logout.html'}, name='logout'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile_view'),
    path('change_password/', views.change_password, name = 'change_password_view'),
]
