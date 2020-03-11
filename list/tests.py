#############################
# tests.py
# Gordon Zuehlke 3-11-20
#############################

from django.urls import resolve
from django.test import TestCase
from list.views import home_page

class HomePageTest(TestCase):

    def test_root_url_reselves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)






