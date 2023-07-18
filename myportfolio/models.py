from django.db import models


class Project(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='projects')
	description = models.CharField(max_length=500)

	class Meta:
		verbose_name_plural='Projects'

	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	message =models.TextField()

	def __str__(self):
		return self.name




