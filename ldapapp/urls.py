"""
URL configuration for ldapapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# urls.py

# project/urls.py

from django.contrib import admin
from django.urls import path, include
from ldapauth.views import login, logout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ldapauth.urls')),  # Include the URL patterns from your app
    path('login/', login, name='login'),  # Include the URL pattern for the login view
    path('logout/', logout, name='logout'),  # Include the URL pattern for the logout view
    path('home/', home, name='home'),  # Include the URL pattern for the home view
]
