from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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


		elif 'username' in request.POST:  
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username=username, password=password)
			if user is not None:  # user exists  
				login(request, user)
				context = {}
				context['user_authenticated'] = 'True'
				context['universities'] = Universities.objects.all()
			
			else: # no user exists
				context['user_authenticated'] = 'false'
				messages.error(request, 'Hey ' + username + ', we appreciate your login try. But would you please check your username and password once more?')

			return render(request, 'home.html', context)


		elif 'new_username' in request.POST: # sign up checking
			new_username = request.POST['new_username']
			new_email    = request.POST['new_email']
			new_password = request.POST['new_password']

			context = {}
			username_checking = 0
			try:
				username_checking = len(User.objects.filter(username=new_username))
			except:
				username_checking = 0
			
			email_checking = 0
			try:
				email_checking = len(User.objects.filter(email=new_email))
			except:
				email_checking = 0

			# if username_checking > 0 or  email_checking > 0 then user exists
			if username_checking + email_checking > 0:
				messages.error(request, 'Requested ' + ('username' if username_checking > 0 else 'email') + ' already exists')
				context['user_authenticated'] = 'false'
			
			else: # no user exists with requested username & password. Safe to proceed
				new_user = User.objects.create_user(username=new_username, 
													email=new_email,
													password=new_password)
				new_user.save()
				user = authenticate(request,username=new_username,
											password=new_password)
				if user is not None: # user exists - ready to login
					login(request, user)
					request.session['PASSWORD'] = new_password # For API data access purpose
					
					collect_api(request)
					context['user_authenticated'] = 'true'
					context['countries'] = Countries.objects.all()
					messages.success(request, 'Congratulations ' + new_username + '!!! You are now a member of our Countries!!! family')
				else: # new user vanished from database 
					context['user_authenticated'] = 'false'
					messages.error(request, 'Hurry ' + new_username + '.... Your account has been deleted by someone from database...')
			
			return render(request, 'home.html', context)


		elif 'logout' in request.POST:
			logout(request) # logging a user out
			return redirect(reverse('home'), permanent=True)