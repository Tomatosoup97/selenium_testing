from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.View.as_view() , name='index'),
]