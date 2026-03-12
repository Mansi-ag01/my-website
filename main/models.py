from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    roll_no = models.CharField(max_length=20, unique=True)
    semester = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    father_phone = models.CharField(max_length=15, blank=True)
    mother_phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.name or 'No Name'} ({self.roll_no})"

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, default='Assistant Professor')
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='faculty_photos/', blank=True, null=True)
    cv = models.FileField(upload_to='faculty_cv/', blank=True, null=True)
    experience = models.IntegerField(default=0)
    qualifications = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name() if self.user else 'No User'}"

class Result(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.roll_no} - {self.subject}"

class Facility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StudentAdmission(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    class_applying = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.father_name}"
