from django.test import TestCase
from django.contrib.auth import get_user_model
from laconicurls.models import Shortcut, laconic_url_for_object


class BaseTestCase(TestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user('test','test@example.com')

    def tearDown(self):
        #clean up users
        self.user_model.objects.all().delete()
        Shortcut.objects.all().delete()

class UserLinkTests(BaseTestCase):

    def test_simple_shortcut(self):
        url = laconic_url_for_object(self.user)
        res = self.client.get(url)
        self.assertRedirects(res, self.user.get_absolute_url(), status_code=301)

    def test_no_duplicates(self):
        url1 = laconic_url_for_object(self.user)
        url2 = laconic_url_for_object(self.user)
        self.assertEquals(url1, url2)

    def test_not_found(self):
        short_url = laconic_url_for_object(self.user)
        self.user.delete()
        res = self.client.get(short_url)
        self.assertEquals(res.status_code, 404)

    def test_case_insensitive(self):
        short_url = laconic_url_for_object(self.user)
        for u in [short_url.lower(), short_url.upper()]:
            self.assertRedirects(self.client.get(u), self.user.get_absolute_url(), status_code=301)

class BadLinkTests(BaseTestCase):

    def test_no_link_to_shortcut(self):
        s1 = Shortcut(content_object = self.user)
        s1.save()
        self.assertRaises(Shortcut.InvalidLinkObject, laconic_url_for_object, s1)

