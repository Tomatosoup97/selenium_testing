# -*- coding: utf-8 -*-
import datetime
from hashlib import sha256
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import OrderForm
from .models import Order

class OrderView(CreateView):
	template_name = "order/order.html"
	form_class = OrderForm

	def form_valid(self, form):
		form.instance.date = timezone.now()
		form.save()
		word = str(form.instance.date) + str(form.instance.id) \
				+ form.instance.email + form.instance.product.name
		key = sha256(word.encode('utf-8')).hexdigest()
		form.instance.activation_key = key
		form.save()
		return super(OrderView, self).form_valid(form)

	def get_success_url(self):
		return reverse('order:success', args=(self.object.id,))

class SuccessView(TemplateView):
	template_name = "order/success.html"

def order_confirmation(request, activation_key):
	order = get_object_or_404(Order, activation_key=activation_key)
	key_expires = order.date + datetime.timedelta(1/12)
	message = ""
	if order.is_activated:
		message = "This order have already been confirmed"
	elif key_expires < timezone.now():
		message = "This order key has expired"
	else:
		order.is_activated = True
		order.save()
		message = "Your order have been confirmed. {}".format(order.is_activated)
	return render_to_response('order/activated_key.html', {'message': message})