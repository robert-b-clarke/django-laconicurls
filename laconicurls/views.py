from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, Http404
from laconicurls.models import Shortcut

def follow(request, base27_id):
    try:
        shortcut = Shortcut.from_base27_id(base27_id.upper())
    except Shortcut.DoesNotExist:
        raise Http404

    target = shortcut.content_object
    if target:
        return HttpResponsePermanentRedirect(target.get_absolute_url())
    #no target available
    raise Http404
