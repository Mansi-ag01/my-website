from django.contrib import admin
from .models import Student, Faculty, Result, Facility, StudentAdmission

# ✅ StudentAdmin - ONLY ONE!
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'father_name', 'mother_name', 'father_phone']
    search_fields = ['name', 'roll_no', 'father_name', 'mother_name']

# ✅ StudentAdmissionAdmin - Form submissions
@admin.register(StudentAdmission)
class StudentAdmissionAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'father_name', 'mother_name', 'phone', 'class_applying']
    search_fields = ['student_name', 'father_name', 'mother_name', 'phone']

# ✅ Faculty
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'user', 'department', 'phone']

# ✅ Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks', 'grade']

# ✅ Facility
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
