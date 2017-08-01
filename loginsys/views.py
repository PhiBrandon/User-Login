from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .forms import loginForm

# Create your views here.
class loginView(View):
	template_name = 'loginsys/login.html'
	form = loginForm()
	def get(self, request, *args, **kwargs):
		#form = loginForm()
		return render(request, self.template_name, {'login':self.form})

	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request,'loginsys/welcome.html')
		else:
			error = "There was an error logging in."
			return render(request, self.template_name, {'login':self.form, 'error':error})

class registerView(View):
	template_name = 'loginsys/register.html'
	def get(self, request, *args, **kwargs):
		form = UserCreationForm()
		return render(request, 'loginsys/register.html', {'register':form})
	def post(self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			lform = loginForm()
			return render(request, 'loginsys/login.html',{'login':lform,'success': "registration successful!"})
		else:
			form = UserCreationForm()
			return render(request, 'loginsys/register.html',{'register':form,"error":"there was an error!"})
