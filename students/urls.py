from django.urls import path

from . import views
from .views import StudentCreateView, StudentListView, StudentUpdateView


urlpatterns = [
	path('', StudentListView.as_view(), name='student_list'),
	path('add/', StudentCreateView.as_view(), name='student_add'),
	path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),

]


