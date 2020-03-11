###############################
# functional_tests.py
# Gordon Zuehlke 3-11-20
###############################

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online To-Do app
        # She goes to check out its home page
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away.
        # She types,"Buy peacock feathers" into an app text box.
        # (Edith's hobby is fly fishing lures.)
        # When she hits enter, the page updates and now lists 
        # "1: Buy peacock feather" as an item in a to-do list.
        # There is still a text box inviting her to enter another item.
        # She enters, "Use peacock feathers to make a fly."
        # The page updates again and shows both items.
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        # She visits that URL - her to-do list is still there.
        # Satisfied, she goes back to sleep 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
  


