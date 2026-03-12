from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student, Faculty, Result, Facility, StudentAdmission
from .forms import AdmissionForm, ContactForm


# ===============================
# PUBLIC PAGES
# ===============================

def home(request):
    return render(request, 'main/home.html')


def admission(request):

    if request.method == 'POST':
        form = AdmissionForm(request.POST)

        if form.is_valid():
            form.save()   # save to database
            messages.success(request, "Application Received Successfully!")
            return redirect('admission')

    else:
        form = AdmissionForm()

    return render(request, 'main/admission.html', {'form': form})


def dashboard(request):

    context = {
        'total_students': Student.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_admins': User.objects.filter(is_staff=True).count(),
    }

    return render(request, 'main/dashboard.html', context)


def facilities(request):
    return render(request, 'main/facilities.html')


def faculties(request):
    return render(request, 'main/faculties.html')


def management(request):
    return render(request, 'main/management.html')


# ===============================
# CONTACT PAGE
# ===============================

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(request, "Message Sent Successfully!")
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


# ===============================
# AUTHENTICATION
# ===============================

def login_view(request):

    role = request.GET.get('role', 'guest')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if user.is_staff or user.is_superuser:
                return redirect('admin_panel')

            elif Student.objects.filter(user=user).exists():
                return redirect('student_portal')

            elif Faculty.objects.filter(user=user).exists():
                return redirect('faculty_portal')

            else:
                messages.error(request, "Profile not found!")
                return redirect('login')

        else:
            return render(request, 'main/login.html', {
                'error': 'Invalid credentials!',
                'role': role
            })

    return render(request, 'main/login.html', {'role': role})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


# ===============================
# REGISTER ADMIN
# ===============================

@login_required
def register(request):

    if not request.user.is_superuser:
        messages.error(request, "Super admin access required!")
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()

        messages.success(request, "New admin created successfully!")
        return redirect('admin_panel')

    return render(request, 'main/register.html')


# ===============================
# ADMIN PANEL
# ===============================

@login_required
def admin_panel(request):

    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, "Admin access required!")
        return redirect('home')

    context = {

        'total_students': Student.objects.count(),
        'total_faculty': Faculty.objects.count(),
        'total_results': Result.objects.count(),
        'total_facilities': Facility.objects.count(),
        'total_admissions': StudentAdmission.objects.count(),
        'recent_students': Student.objects.all()[:5],

    }

    return render(request, 'main/admin_dashboard.html', context)


# ===============================
# STUDENT PORTAL
# ===============================

@login_required
def student_portal(request):

    try:

        student = Student.objects.get(user=request.user)

        context = {
            'student': student,
            'results': Result.objects.filter(student=student),
            'total_results': Result.objects.filter(student=student).count(),
        }

        return render(request, 'main/student_portal.html', context)

    except Student.DoesNotExist:

        messages.error(request, "Student profile not found!")
        return redirect('home')


# ===============================
# FACULTY PORTAL
# ===============================

@login_required
def faculty_portal(request):

    try:

        faculty = Faculty.objects.get(user=request.user)

        context = {
            'faculty': faculty,
            'my_students': Student.objects.all(),
        }

        return render(request, 'main/faculty_portal.html', context)

    except Faculty.DoesNotExist:

        messages.error(request, "Faculty profile not found!")
        return redirect('home')