from django import forms
from doctors.models import Doctors, ReportDoctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['name','cedule','phone','direction']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cedule': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class ReportDoctorForm(forms.ModelForm):
    class Meta:
        model = ReportDoctor
        fields = ['doctor','medicament','patient_name','patient_Cedule',"patient_phone"]
        widgets = {
            'doctor': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medicament': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'patient_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'patient_Cedule': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'patient_phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }