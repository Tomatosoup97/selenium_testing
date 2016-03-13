from django import forms
from order.models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('name', 'surname', 'email', 'quantity', 'product')