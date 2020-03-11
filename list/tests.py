#############################
# tests.py
# Gordon Zuehlke 3-11-20
#############################

from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)






