"""Django URL Configuration

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
from django.urls import path, re_path
from Study import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student', views.get_student_list, name='showStudent'),
    path('module', views.get_module_list, name='showModul'),
    path('studiengang', views.get_studiengang_list, name='showStudiengang'),
    path('student/add', views.manipulate_student, name='addStudent'),
    re_path(r'^student/edit/(?P<pk>[0-9]+)/?$', views.manipulate_student, name='editStudent')
]
