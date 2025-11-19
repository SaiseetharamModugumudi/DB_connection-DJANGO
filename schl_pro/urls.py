"""
URL configuration for schl_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import student_list, student_form, home
from app1.views import update_Student, delete_Student


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('student_form/', student_form, name='student_form'),
    path('student_form/<str:name>/', update_Student, name='update_Student'),
    path('delete_student/<str:name>/', delete_Student, name='delete_Student'),
]
