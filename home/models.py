from django.db import models

# Create your models here.
class API_token(models.Model):  
	username = models.CharField(max_length=150)
	token    = models.CharField(max_length=32)