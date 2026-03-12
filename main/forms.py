from django import forms
from .models import StudentAdmission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = StudentAdmission
        fields = ['student_name', 'father_name', 'mother_name', 'class_applying', 'phone', 'email', 'address']
        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter full name'
            }),
            'father_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': "Father's full name"
            }),
            'mother_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': "Mother's full name"
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '+91 12345 67890'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'parent@example.com'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'rows': 3,
                'placeholder': 'Full residential address'
            }),
        }

    # ✅ FIXED: Custom ChoiceField for class dropdown
    class_applying = forms.ChoiceField(
        choices=[
            ('PG', 'Play Group'),
            ('LKG', 'LKG'),
            ('UKG', 'UKG'),
            ('I', 'Class I'),
            ('II', 'Class II'),
            ('III', 'Class III'),
            ('IV', 'Class IV'),
            ('V', 'Class V')
        ],
        widget=forms.Select(attrs={
            'class': 'form-select form-select-lg'
        }),
        required=True
    )


class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your message'
        })
    )