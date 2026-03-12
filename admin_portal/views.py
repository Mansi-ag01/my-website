from django.shortcuts import render
from .models import Admission, Student, Faculty, Result

def dashboard(request):

    total_students = Student.objects.count()
    total_faculty = Faculty.objects.count()
    total_results = Result.objects.count()
    total_admissions = Admission.objects.count()

    context = {
        'total_students': Student.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_results': Result.objects.count(),
        'total_facilities': Facility.objects.count(),

        'all_admissions': StudentAdmission.objects.all().order_by('-id'),
        'total_admissions': StudentAdmission.objects.count(),

        'recent_students': Student.objects.all()[:5],
    }
    return render(request, 'dashboard.html', context)