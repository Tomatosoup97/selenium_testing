from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.FormSubmissionView.as_view() , name='index'),
	url(r'^$', views.SuccessView.as_view() , name='success'),
]