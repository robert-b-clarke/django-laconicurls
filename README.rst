===================
Django Laconic URLS
===================

.. image:: https://travis-ci.org/robert-b-clarke/django-laconicurls.svg?branch=master
    :target: https://travis-ci.org/robert-b-clarke/django-laconicurls

Another URL shortner for Django?
--------------------------------

This one is a bit different to the others. It uses Django's GenericForeignKeys and get_absolute_url to provide short urls for instances of Django models. The goal is to provide short, human readable urls, that can be featured within emails, print campaigns, qr codes and social media etc. These URLs will continue to work across site restructures etc 

Quick start
-----------

1. Add "laconicurls" to INSTALLED_APPS in settings.py::
   
    INSTALLED_APPS = (
        ...
        'laconicurls',
    )

2. Add laconicurls urlconf to urls.py. If possible it's best to use a single case insensitive letter for this::

    url(r'^(?i)Z', include('laconicurls.urls')),

3. Run `python manage.py migrate` to create the necessary models.

4. Create some urls::

    from laconicurls.models import laconic_url_for_object
    #this can be any django object that supports get_absolute_url
    article = MyArticleModel.objects.get(pk=1)
    short_url = laconic_url_for_object(article)
