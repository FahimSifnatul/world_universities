from django.shortcuts import render
from django.views import View
import requests

# custom models, serializers  
from universities_api.models import Universities

API_URL = 'http://127.0.0.1:8000/'


# Create your views here.
class Home(View):  
	def get(self, request, *args, **kwargs):
		universities = Universities.objects.all().order_by('country')

		if len(universities) == 0: 
			# To build the database
			requests.get(API_URL+'collect')
			universities = Universities.objects.all().order_by('country')

		context = {}
		context = {'universities' : universities}
		return render(request, 'home.html', context)