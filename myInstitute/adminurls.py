from django.conf.urls import include, url, patterns
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
	
	url(r'^/?$','common.adminviews.dashboard',name='dashboard'),#PORTAL HOME
	url(r'^users/',include('usermgmt.adminurls')),
)