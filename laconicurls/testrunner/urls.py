import os
from django.contrib import admin
from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^(?i)Z', include('laconicurls.urls')),
)

