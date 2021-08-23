from django.shortcuts import render
from django.views import View
import requests

# custom models, serializers  
from universities_api.models import Universities

# Create your views here.
class Home(View):  
	def get(self, request, *args, **kwargs):
		universities = Universities.objects.all()

		if len(universities) == 0: 
			url = 'http://universities.hipolabs.com/search'
			universities_list = requests.get(url).json()
			values = []
			for university in universities_list:  
				values.append(Universities(name=university['name'],
											domains = university['domains'][0],
											web_pages = university['web_pages'][0],
											country = university['country'],
											alpha_two_code = university['alpha_two_code']))
			Universities.objects.bulk_create(values)

		context = {}
		context = {'universities' : universities}
		return render(request, 'home.html', context)