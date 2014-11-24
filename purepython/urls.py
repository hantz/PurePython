from django.conf.urls import patterns, include, url
from django.contrib import admin

from fb.views import index
from fb.views import post_page

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)$', post_page, name='post'),
    url(r'^admin/', include(admin.site.urls)),
)
