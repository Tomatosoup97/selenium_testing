from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view() , name='index'),
	url(r'sign-in/$', views.SignInView.as_view() , name='sign_up'),
	url(r'sign-up/$', views.SignUpView.as_view() , name='sign_in'),
	url(r'account-created/$',
		views.CreatedUserView.as_view() , name='created'),
	url(r'(?P<slug>\w+)/$',
		views.UserProfileView.as_view(), name='profile'),
	url(r'login-to-page', views.login_view, name="login_page")
]