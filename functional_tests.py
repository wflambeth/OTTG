from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Person is looking for a badass to-do app. They check the web page
        self.browser.get('http://localhost:8000')

        # They notice that the page title & header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # They're invited to enter a to-do item straightaway. 
        
        # They type "Buy peacock feathers" into a text box.

        # When they hit enter, the page updates and now lists "1: Buy peacock feathers" 
        # as item in list. 

        # Text box inviting them to add another item remains. 
        # They enter "Use peacock feathers to make a fly"

        # The page updates and now shows both items on the list. 

        # Person sees that the site has generated a unique URL for them; 
        # this is accompanied by some explanatory text to that effect. 

        # They visit the URL and see their to-do list is still there. 

        # They exit the browser.

if __name__ == '__main__':
    unittest.main(warnings='ignore')