from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from laconicurls.obfuscation import base27_encode, base27_decode
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

class Shortcut(models.Model):
    """An item for which we have created a short url"""
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    #class var for caching content type id
    _content_type = None

    class Meta:
        unique_together = ('content_type', 'object_id')

    def get_absolute_url(self):
        #use reverse and obfu id
        return reverse('laconicurls.views.follow', kwargs={'base27_id': base27_encode(self.id)})

    @classmethod
    def from_base27_id(cls, base27_id):
        """Class method, accept a base27 id and return the corresponding Shortcut instance"""
        return cls.objects.get(pk=base27_decode(base27_id))

    @classmethod
    def get_content_type(cls):
        """Shortcut to get the contenttype of this class. Uses a local class level cache to prevent constant db lookups"""
        if not cls._content_type:
            cls._content_type = ContentType.objects.get_for_model(cls)
        return cls._content_type

    class InvalidLinkObject(Exception):
        pass

def shortcut_pre_save_hook(sender, instance, *args, **kwargs):
    #prevent users from saving links to links
    if sender.get_content_type() == instance.content_type:
        raise sender.InvalidLinkObject

pre_save.connect(shortcut_pre_save_hook, sender=Shortcut) 

def laconic_url_for_object(obj):
    """Take an object, find or create a shortcut, and return the url for the shortcut"""
    try:
        shortcut = Shortcut.objects.get(
                object_id = obj.pk,
                content_type = ContentType.objects.get_for_model(obj)
        )
    except Shortcut.DoesNotExist:
        shortcut = Shortcut(content_object=obj)
        shortcut.save()

    return shortcut.get_absolute_url()


