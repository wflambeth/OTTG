from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomepageTest(TestCase):

    def test_rool_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
