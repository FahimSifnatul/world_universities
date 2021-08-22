from rest_framework import serializers  

# custom 
from .models import Universities  

class UniversitiesSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Universities  
		fields = '__all__'