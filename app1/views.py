from django.shortcuts import render,redirect
from .models import Learners
from .models import Employee
from .models import Batch
from .models import Department

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

def add_student(req):
    if req.method == 'POST':
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        contact = req.POST['phone']
        dob = req.POST['dob']
        qualification = req.POST['qualification']
        gender = req.POST['gender']

        # print(fname,lname,email,contact,dob,qualification,gender)
        learner = Learners.objects.create(first_name=fname,last_name=lname,email=email,phone=contact,dob=dob,qualification=qualification,gender=gender)
        learner.save()
        return redirect('student-dashboard')

    else:
        print('This is a get method')
    return render(req,'add_student.html')

def add_employee(req):
    departments = Department.objects.all()
    context = {
        'departments':departments
    }
    if req.method == 'POST':
        eid = req.POST['id']
        name = req.POST['name']
        email = req.POST['email']
        contact = req.POST['contact']
        dob = req.POST['dob']
        department = req.POST['department']
        role = req.POST['role']
        gender = req.POST['gender']
        
        department_object = Department.objects.get(id=department)

        # print(fname,lname,email,contact,dob,qualification,gender)
        employee = Employee.objects.create(employee_id=eid,employee_name=name,employee_email=email,employee_phone=contact,dob=dob,department=department,role=role,gender=gender)
        employee.save()
        return redirect('employee-dashboard')

    else:
        print('This is a get method')
    return render(req,'add_employee.html',context)