from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail

class HomeView(TemplateView):
	template_name = "apps_manager/index.html"