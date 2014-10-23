from django.test import TestCase
from laconicurls.models import Shortcut, laconic_url_for_object
from django.db import models
from django.utils.http import urlquote

class NonsenseQuotation(models.Model):
    """A dummy model that implements get_absolute_url"""
    quote = models.TextField()

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return "/stupid-quotations/%s/" % urlquote(self.quote)

class BaseTestCase(TestCase):

    def setUp(self):
        self.quotation = NonsenseQuotation.objects.create(quote="I wander lonely as a cloud")

    def assertRedirectsWithoutCaringAbout404(self, *args, **kwargs):
        """A messy workaround to prevent the test client complaining about not being able to find the final url, which we don't actually care about"""
        try:
            self.assertRedirects(*args, **kwargs)
        except AssertionError:
            self.assertRedirects(*args, target_status_code=404, **kwargs)


    def tearDown(self):
        #clean up db
        NonsenseQuotation.objects.all().delete()
        Shortcut.objects.all().delete()

class UserLinkTests(BaseTestCase):

    def test_simple_shortcut(self):
        url = laconic_url_for_object(self.quotation)
        res = self.client.get(url, follow=True)
        res.redirect_chain[0][0]
        self.assertRedirectsWithoutCaringAbout404(res, self.quotation.get_absolute_url(), status_code=301)

    def test_no_duplicates(self):
        url1 = laconic_url_for_object(self.quotation)
        url2 = laconic_url_for_object(self.quotation)
        self.assertEquals(url1, url2)

    def test_not_found(self):
        short_url = laconic_url_for_object(self.quotation)
        self.quotation.delete()
        res = self.client.get(short_url)
        self.assertEquals(res.status_code, 404)

    def test_case_insensitive(self):
        short_url = laconic_url_for_object(self.quotation)
        for u in [short_url.lower(), short_url.upper()]:
            self.assertRedirectsWithoutCaringAbout404(self.client.get(u), self.quotation.get_absolute_url(), status_code=301)

class BadLinkTests(BaseTestCase):

    def test_no_link_to_shortcut(self):
        s1 = Shortcut(content_object = self.quotation)
        s1.save()
        self.assertRaises(Shortcut.InvalidLinkObject, laconic_url_for_object, s1)

