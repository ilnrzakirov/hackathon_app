from django import forms

from .models import Student


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email"]