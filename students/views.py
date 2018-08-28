# Some pieces are borrowed from https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from students.models import Student
from students.forms import StudentForm


class StudentListView(ListView):
	model = Student
	context_object_name = 'students'


class StudentCreateView(CreateView):
	model = Student
	fields = ('name', 'animal', 'language')
	success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_update_form.html'
    success_url = reverse_lazy('student_list')
