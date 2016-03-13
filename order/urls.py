from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.OrderView.as_view() , name='index'),
	url(r'^thank-you$', views.SuccessView.as_view() , name='success'),
	url(r'^confirmation/(?P<activation_key>\w+)/$',
		views.order_confirmation, name='confirm'),
]