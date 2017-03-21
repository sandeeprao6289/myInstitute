from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myInstitute.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admincp/', include(admin.site.urls)),
    url(r'^admin/', include('myInstitute.adminurls')),

    url(r'^/?$', 'common.views.home', name='site_home'),
]
