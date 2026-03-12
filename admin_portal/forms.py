from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class':'form-control'}),
            'father_name': forms.TextInput(attrs={'class':'form-control'}),
            'mother_name': forms.TextInput(attrs={'class':'form-control'}),
            'class_applying': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
        }