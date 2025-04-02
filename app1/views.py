from django.shortcuts import render,redirect
from .models import Learners
from .models import Employee
from .models import Batch

# Create your views here.

def index(req):
    return render(req,'index.html')

def student_dashboard(req):
    students = Learners.objects.all()
    context={
        'students':students
    }
    return render(req,'student_dashboard.html',context)

def employee_dashboard(req):
    employees = Employee.objects.all()
    context={
        'employees':employees
    }
    return render(req,'employee_dashboard.html',context)

def batch(req):
    batches = Batch.objects.all()
    context={
        'batches':batches
    }
    return render(req,'batch.html',context)

def student_profile(req,id):
    student = Learners.objects.get(id=id)
    context={
        'student':student
    }
    print(student)
    return render(req,'student_profile.html',context)

def delete_student(req,id):
    student = Learners.objects.get(id=id)
    student.delete()
    return redirect('student-dashboard')

def add_student(req):
    return render(req,'add_student.html')