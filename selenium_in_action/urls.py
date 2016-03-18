"""
selenium_in_action URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^order/', include('order.urls', namespace="order")),
    url(r'^user/', include('user.urls', namespace="user")),
    url(r'^', include('apps_manager.urls', namespace="home")),
]