from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Customer(models.Model):
	c_name=models.CharField(max_length=20)
	c_password=models.CharField(max_length=10)
	c_phone_no=models.IntegerField()
	c_email_id=models.EmailField(max_length=50)
	c_address= models.CharField(max_length=50)

	def __str__(self):
		return self.c_name

class tasker(models.Model):
	t_name=models.CharField(max_length=20)
	t_password=models.CharField(max_length=10)
	t_phone_no=models.IntegerField() 
	t_email=models.CharField(max_length=20)
	t_type= models.CharField(max_length=15)
	t_location= models.CharField(max_length=20)
	t_rupee=models.IntegerField()
	t_address=models.CharField(max_length=50)

	def __str__(self):
		return self.t_name