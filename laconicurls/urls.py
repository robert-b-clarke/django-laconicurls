from django.conf.urls import patterns
from laconicurls.obfuscation import BASE27_ALPHABET

urlpatterns = patterns('',
    (r'^(?i)(?P<base27_id>[' + BASE27_ALPHABET + ']+)$', 'laconicurls.views.follow')
)
