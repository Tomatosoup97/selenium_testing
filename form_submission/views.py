from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.core.mail import send_mail

class FormSubmissionView(FormView):
	template_name = "form_submission/form_submission.html"

class SuccessView(TemplateView):
	template_name = "form_submission/success.html"