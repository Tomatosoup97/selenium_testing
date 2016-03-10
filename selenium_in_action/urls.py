"""selenium_in_action URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^order/', include('order.urls')),
    url(r'^form/', include('form_submission.urls'))
    url(r'^search_box/', include('search_box.urls'))
    url(r'^', include('apps_manager.urls'))
]