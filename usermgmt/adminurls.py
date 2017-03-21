from django.conf.urls import *
from django.views.generic.base import RedirectView

urlpatterns = patterns('usermgmt.adminviews',

	url(r'^/?$','users_list_view',name='users'),
	url(r'^load-users/?$','ajax_load_users',name='ajax_load_users'),
	url(r'^new/$','user_add_view',name='add_user'),
	url(r'^delete/$','user_delete_view',name='delete_user'),
)