from django import forms
from pastillas.models import medicine


class medicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['name','description','price','stock']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
