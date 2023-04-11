from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django_auth_ldap.backend import LDAPBackend

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        ldap_backend = LDAPBackend()
        user = ldap_backend.authenticate(request, username=username, password=password)
        if user is not None:
            ldap_backend.populate_user(user)
            return redirect('home') # Replace 'home' with the URL name of your homepage
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
