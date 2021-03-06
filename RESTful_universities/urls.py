"""RESTful_universities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers  

# custom
from universities_api.views import API, ListUniversities, SearchUniversities,\
                                    SearchByCountryUniversities,\
                                    CollectUniversities
from home.views import Home

router = routers.SimpleRouter()
router.register(r'universities', API)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('', include(router.urls)),
    path('<api_token>/collect', CollectUniversities.as_view(), name='collect-universities'),
    path('<api_token>/list', ListUniversities.as_view(), name='list-universities'),
    path('<api_token>/search/<university>', SearchUniversities.as_view(), name='search-universities'),
    path('<api_token>/search-by-country/<country>', SearchByCountryUniversities.as_view(), name='search-by-country-universities'),
    path('admin/', admin.site.urls),
]
