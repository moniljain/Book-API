from django.db import models

# Create your models here.
class Book(models.Model):
	name=models.CharField(max_length=255)
	genre=models.CharField(max_length=255)
	author=models.CharField(max_length=255)
	owner = models.ForeignKey('auth.User',related_name='books',on_delete=models.CASCADE,null=True)
	
	
	def __str__(self):
		return "{}".format(self.name)