from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.hello.urls import urlpatterns as hello_patterns

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include(hello_patterns)),
    url(r'^admin/', include(admin.site.urls)),
)
