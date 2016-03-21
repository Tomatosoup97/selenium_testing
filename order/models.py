from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name

class Order(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField()
	quantity = models.IntegerField(default=1)
	product = models.ForeignKey(Product, related_name='order')
	activation_key = models.CharField(max_length=200)
	is_activated = models.BooleanField(default=False)
	date = models.DateTimeField()

	def __str__(self):
		return "Order number: {}".format(self.id)