# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Faculty, Student, Result


@login_required
def faculty_dashboard(request):
    faculty = Faculty.objects.get(user=request.user)
    students = Student.objects.all()
    recent_results = Result.objects.all().order_by('-exam_date')[:20]

    return render(request, 'faculty/dashboard.html', {
        'faculty': faculty,
        'students': students,
        'recent_results': recent_results
    })

