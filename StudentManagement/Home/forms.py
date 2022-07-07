from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'student': 'Student Number',
            'fullName': 'Full name',
            'birthday': 'Birthday',
            'phone': 'Phone',
            'email': 'Email',
            'address': 'Address',
        }

        widgets = {
            'student': forms.NumberInput(attrs={'class': 'form-control'}),
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
