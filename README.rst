===================
Django Laconic URLS
===================

.. image:: https://travis-ci.org/robert-b-clarke/django-laconicurls.svg?branch=master
    :target: https://travis-ci.org/robert-b-clarke/django-laconicurls

.. image:: https://pypip.in/v/django-laconicurls/badge.png
    :target: https://pypi.python.org/pypi//django-laconicurls/
    :alt: Downloads

Introduction
------------

django-laconicurls is different to other Django URL Shortener apps. It uses Django's GenericForeignKeys and get_absolute_url to provide short urls for instances of Django models. The goal is to provide short, human readable urls, that can be featured within emails, print campaigns, qr codes and social media etc. These URLs will continue to work across site restructures etc 

Quick start
-----------
1. Run `pip install django-laconicurls` to install django-laconicurls

2. Add "laconicurls" to INSTALLED_APPS in settings.py::
   
    INSTALLED_APPS = (
        ...
        'laconicurls',
    )

3. Add laconicurls urlconf to urls.py. If possible it's best to use a single case insensitive character for this::

    url(r'^(?i)Z', include('laconicurls.urls')),

4. Run `python manage.py migrate` to create the necessary models.

5. In your code, create some urls::

    from laconicurls.models import laconic_url_for_object
    #this can be any django object that supports get_absolute_url
    article = MyArticleModel.objects.get(pk=1)
    short_url = laconic_url_for_object(article)

Features
--------

 * Creates and manages shortcut URLs for any instance of a Django model that implements get_absolute_url

 * Case insensitive Base27 encoding of URLs. Alphabet excludes vowels and numbers which look like vowels to reduce the likelyhood of offensive URLs (at least in English)

 * One laconic URL per object. Repeat calls to `laconic_url_for_object` for a given object will always result in the same URL  

Example Usage
-------------

Say you have two models, Product and Promotion, which both implement get_absolute_url and have search engine friendly URLs::
    
    >>> Product.objects.get(pk=100).get_absolute_url()
    '/products/garden/100-fancy-green-electric-lawnmower'
    >>> Promotion.objects.get(pk=50).get_absolute_url()
    '/promotions-and-hot-deals/50-up-to-twenty-percent-off-gardening-equipment'

Clearly these URLs are not suitable for a print campaign, and are likely to change over time, subject to different SEO trends.

To add support for laconic URLs you need to pick a suitable prefix which doesn't clash with any existing URLs. Ideally this will be a single character and won't be case sensitive, but if you want it can be longer or contain slashes. For example, add the following to your urls.py to have laconicurls that begin with the letter Q::

    url(r'^(?i)Q', include('laconicurls.urls')),

The easiest way to get laconic urls is to use the `laconic_url_for_object` helper. Example output might be as follows::
    
    >>> from laconicurls.models import laconic_url_for_object
    >>> laconic_url_for_object(Product.objects.get(pk=100))
    '/QGH3'
    >>> laconic_url_for_object(Promotion.objects.get(pk=50))
    '/QGH4'

When accessed these URLs will redirect to the locations returned by their respectve get_absolute_url method calls

TODO
----

 * Add support for templatetags
 * Investigate ways to support alternate alphabets, as some users will not require case insensitive urls and may prefer a more efficient encoding (e.g. base 62)
 * Management commands for inspecting URLs
