"""ProjectCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from AppCMS import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('AppCMS.urls')),
    path('index/',views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

    path('counter/', views.counter, name='counter'),
    path('change_password_g/', views.change_password_g, name='change_password_g'),
    path('register/', views.register, name='register'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
   # path('dashboard/', views.dashboard, name='dashboard'),
    path('change_password/', views.change_password, name='change_password'),
    path('complaints/', views.complaints, name='complaints'),
    path('list/',views.list, name='list'),
    path('slist/',views.slist, name='slist'),
    path('allcomplaints/', views.allcomplaints, name='allcomplaints'),
    path('solved/', views.solved, name='solved'),
    path('pdf_viewer/', views.pdf_viewer, name='pdf_viewer'),
    path('pdf_view/', views.pdf_view, name='pdf_view'),
   # path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
