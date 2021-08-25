from django.shortcuts import render
from django.views import View
import requests

# custom models, serializers  
from universities_api.models import Universities

API_URL = 'http://127.0.0.1:8000/'


# Create your views here.
class Home(View):  
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			universities = Universities.objects.all().order_by('country')

			if len(universities) == 0: 
				# To build the database
				requests.get(API_URL+'collect')
				universities = Universities.objects.all().order_by('country')

			context = {}
			context['user_authenticated'] = 'True'
			context['universities'] = universities
			return render(request, 'home.html', context)

		else:  
			context = {}
			context['user_authenticated'] = 'False'
			return render(request, 'home.html', context)


	def post(self, request, *args, **kwargs):  
		if 'search_by_university_text' in request.POST:  
			university = request.POST['search_by_university_text']
			if university == '':  
				universities = Universities.objects.all().order_by('country')
			else:
				universities = Universities.objects.filter(
								name__istartswith=university).order_by('country')
			context = {}
			context = {'universities' : universities}
			return render(request, 'home.html', context)
		
		elif 'search_by_country_text' in request.POST:
			country = request.POST['search_by_country_text']
			if university == '':  
				universities = Universities.objects.all().order_by('country')
			else:
				universities = Universities.objects.filter(
								country__istartswith=country).order_by('country')  
			context = {}
			context = {'universities' : universities}
			return render(request, 'home.html', context)