# -*- coding: utf-8 -*-
import datetime

from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
	template_name='user/index.html'

class SignUpView(CreateView):
	form_class=UserCreationForm
	template_name='user/register.html'
	success_url = 'success'

class SuccessView(TemplateView):
	template_name = "user/success.html"

class SignInView(TemplateView):
	template_name='user/index.html'
