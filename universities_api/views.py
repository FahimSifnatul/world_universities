from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# custom models, serializers
from .models import Universities
from .serializers import UniversitiesSerializer


# Create your views here.
class API(ModelViewSet):  
	queryset = Universities.objects.all()
	if len(queryset) == 0:
		url = 'http://universities.hipolabs.com/search'
		universities = requests.get(url).json()
		values = []
		for university in universities:  
			values.append(Universities(name=university['name'],
										domains = university['domains'][0],
										web_pages = university['web_pages'][0],
										country = university['country'],
										alpha_two_code = university['alpha_two_code']))
		Universities.objects.bulk_create(values)

	serializer_class = UniversitiesSerializer


class CollectUniversities(APIView):  
	def get(self, request, *args, **kwargs): 
		universities = Universities.objects.all()
		universities.delete()

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

		universities = Universities.objects.all()
		universities_serializer = UniversitiesSerializer(universities, many=True)

		return Response(universities_serializer.data)



class ListUniversities(APIView):   
	def get(self, request, *args, **kwargs):  
		universities = Universities.objects.all()
		universities_serializer = UniversitiesSerializer(instance=universities, many=True)
		return Response(universities_serializer.data) 



class SearchUniversities(APIView):  
	def get(self, request, university, *args, **kwargs):
		universities = Universities.objects.filter(name__istartswith=university)
		universities_serializer = UniversitiesSerializer(instance=universities, many=True)
		return Response(universities_serializer.data)	



class SearchByCountryUniversities(APIView):   
	def get(self, request, country, *args, **kwargs):  
		universities = Universities.objects.filter(country__istartswith=country)
		universities_serializer = UniversitiesSerializer(instance=universities, many=True)
		return Response(universities_serializer.data)
