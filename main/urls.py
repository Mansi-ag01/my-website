from django.urls import path
from . import views

urlpatterns = [
    # PUBLIC
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),

    # PROTECTED
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('student/', views.student_portal, name='student_portal'),
    path('faculty/', views.faculty_portal, name='faculty_portal'),

    # PAGES
    path('admission/', views.admission, name='admission'),
    path('management/', views.management, name='management'),
    path('facilities/', views.facilities, name='facilities'),
    path('faculties/', views.faculties, name='faculties'),
    path('contact/', views.contact, name='contact'),

]