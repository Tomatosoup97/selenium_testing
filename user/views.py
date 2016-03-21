# -*- coding: utf-8 -*-
import datetime

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import RegisterForm

class IndexView(TemplateView):
	template_name = 'user/index.html'

class SignUpView(CreateView):
	form_class = RegisterForm
	template_name = 'user/sign_up.html'

	def get_success_url(self):
		return reverse('user:created')

class SignInView(TemplateView):
	template_name = 'user/sign_in.html'

class CreatedUserView(TemplateView):
	template_name = 'user/created.html'

class UserProfileView(DetailView):
	model = User
	template_name = 'user/profile.html'
	slug_field = 'username'

def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		message = "Signed in successfully"
		return render_to_response(
			'user/login_page.html', {'message': message})
	else:
		message = "Invalid login or password"
		return render_to_response(
			'user/login_page.html', {'message': message})