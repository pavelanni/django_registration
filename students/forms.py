from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'animal', 'language')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
