from django.contrib import admin
from .models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student_name',
        'father_name',
        'mother_name',
        'class_applying',
        'phone',
        'email',
        'created_at'
    )

    search_fields = (
        'student_name',
        'father_name',
        'phone',
        'email'
    )

    list_filter = (
        'class_applying',
        'created_at'
    )

    ordering = ('-created_at',)

    list_per_page = 10