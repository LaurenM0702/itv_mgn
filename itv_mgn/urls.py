"""
URL configuration for itv_mgm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('student-dashboard/',views.student_dashboard,name = 'student-dashboard'),
    path('employee-dashboard/',views.employee_dashboard,name = 'employee-dashboard'),
    path('batch/',views.batch,name = 'batch'),
    path('student-profile/<int:id>/',views.student_profile,name= 'student-profile'),
    path('delete-student/<int:id>',views.delete_student,name= 'delete-student'),
    path('add-student/',views.add_student,name='add-student')
]