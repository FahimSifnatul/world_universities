from django.db import models

# Create your models here.
class Universities(models.Model):  
	name = models.CharField(max_length=128)
	domains = models.CharField(max_length=128)
	web_pages = models.CharField(max_length=128)
	country = models.CharField(max_length=64)
	alpha_two_code = models.CharField(max_length=32)