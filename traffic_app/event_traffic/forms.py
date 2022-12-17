from django import forms

from .models import Student, Feedback


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email"]


class FeedbackForm(forms.ModelForm):
    FEEDBACK = [
        (1, "Очень плохо"),
        (2, "Плохо"),
        (3, "Хорошо"),
        (4, "Отлично"),
        (5, "Супер"),
    ]
    feedback = forms.ChoiceField(choices=FEEDBACK,)

    class Meta:
        model = Feedback
        fields = ["feedback", "description"]
