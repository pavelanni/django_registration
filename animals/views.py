# Some pieces are borrowed from https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from animals.models import Student
from animals.forms import StudentForm


class StudentListView(ListView):
	model = Student
	context_object_name = 'animals'


class StudentCreateView(CreateView):
	model = Student
	fields = ('name', 'animal', 'language')
	success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'animals/student_update_form.html'
    success_url = reverse_lazy('student_list')