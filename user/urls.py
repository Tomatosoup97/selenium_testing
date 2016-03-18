from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'index/$', views.IndexView.as_view() , name='index'),
	url(r'sign-in/$', views.SignInView.as_view() , name='sign_up'),
	url(r'sign-up/$', views.SignUpView.as_view() , name='sign_in'),
	url(r'success/$', views.SuccessView.as_view() , name='success'),
]