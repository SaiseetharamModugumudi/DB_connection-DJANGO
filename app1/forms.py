from app1.models import Students
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model= Students
        fields = '__all__'