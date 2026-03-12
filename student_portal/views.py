# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Result
@login_required
def student_dashboard(request):
    user = request.user
    try:
        student = Student.objects.get(user=user)
        results = Result.objects.filter(student=student).order_by('-exam_date')
    except Student.DoesNotExist:
        return redirect('profile_setup')

    return render(request, 'student/dashboard.html', {
        'student': student,
        'results': results
    })

