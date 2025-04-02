from django.contrib import admin
from .models import Address,Learners,Employee,Course,Department,Batch,Enrollment


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','flat','street','landmark','city','state','pincode']

@admin.register(Learners)
class LearnersAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','dob','phone','qualification','gender','enrollement_date','updated_at','address']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

@admin.register(Batch)
class RegisterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Batch._meta.fields]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Enrollment._meta.fields]