from django.db import models

class Student(models.Model):
	def __str__(self):
		return self.name
		
	name = models.CharField(max_length=30)
	animal = models.CharField(max_length=30)
	language = models.CharField(max_length=30)