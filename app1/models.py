from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]

role_choices = [('trainer','Trainer'),('coordinator','Coordinator'),('other','Other')]

class Address(models.Model):
    INDIAN_STATES = [
        ('ap', 'Andhra Pradesh'),
        ('ar', 'Arunachal Pradesh'),
        ('as', 'Assam'),
        ('br', 'Bihar'),
        ('cg', 'Chhattisgarh'),
        ('ga', 'Goa'),
        ('gj', 'Gujarat'),
        ('hr', 'Haryana'),
        ('hp', 'Himachal Pradesh'),
        ('jk', 'Jammu & Kashmir'),
        ('jh', 'Jharkhand'),
        ('ka', 'Karnataka'),
        ('kl', 'Kerala'),
        ('mp', 'Madhya Pradesh'),
        ('mh', 'Maharashtra'),
        ('mn', 'Manipur'),
        ('ml', 'Meghalaya'),
        ('mz', 'Mizoram'),
        ('nl', 'Nagaland'),
        ('od', 'Odisha'),
        ('pb', 'Punjab'),
        ('rj', 'Rajasthan'),
        ('sk', 'Sikkim'),
        ('tn', 'Tamil Nadu'),
        ('tg', 'Telangana'),
        ('up', 'Uttar Pradesh'),
        ('ut', 'Uttarakhand'),
        ('wb', 'West Bengal'),
        ('an', 'Andaman and Nicobar Islands'),
        ('ch', 'Chandigarh'),
        ('dn', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('dl', 'Delhi'),
        ('ld', 'Lakshadweep'),
        ('py', 'Puducherry'),
    ]

    flat = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    street = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    landmark = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    city = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    state = models.CharField(max_length=255, choices=INDIAN_STATES)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex=r'^\d{6}$')])

class Learners(models.Model):
    
    qualification_choices = [
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('diploma', 'Diploma'),
        ('graduate', 'Graduate'),
        ('post_graduate', 'PG')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    qualification = models.CharField(max_length=255, choices=qualification_choices)
    gender = models.CharField(max_length=10, choices=gender_choices)
    enrollement_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Course (models.Model):
    course_id = models.CharField(max_length=5,primary_key=True)
    course_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255,help_text='input value in month')
    fees = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return f'{self.course_id}-{self.course_name}'

class Department (models.Model):
    department_name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.department_name

class Employee (models.Model):
    employee_id = models.CharField(max_length=5,primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_email = models.EmailField(max_length=255,unique=True)
    employee_phone = models.CharField(max_length=10,validators=[RegexValidator(regex=r'^\d{10}$',message='Enter a valid 10-digit number',code='invalid_phone')])
    dob = models.DateField()
    joining_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10,choices=gender_choices)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True,blank=True)
    role = models.CharField(max_length=255,choices=role_choices)

    def __str__(self):
        return self.employee_name




class Batch(models.Model):
    batch_id = models.CharField(max_length=5,primary_key=True)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_start_date = models.DateField()
    batch_end_date = models.DateField()
    batch_start_time = models.TimeField()
    batch_end_time = models.TimeField()
    trainer = models.ForeignKey(Employee,on_delete=models.RESTRICT,limit_choices_to={'role':'trainer'})
    coordinator = models.ForeignKey(Employee,on_delete=models.RESTRICT,limit_choices_to={'role':'coordinator'},related_name='coordinator')

    def __str__(self):
        return f'{self.batch_id} - {self.course_id}'
 

status_choices = [('active','Active'),('pending','Pending'),('completed','Completed'),('dropped','Dropped')]
class Enrollment(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.RESTRICT)
    learner = models.ForeignKey(Learners,on_delete=models.CASCADE)
    batch_enrolled_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length = 100,choices=status_choices,default='active')

    class Meta:
        unique_together = ('batch','learner')