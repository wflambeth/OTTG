from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # They're invited to enter a to-do item straightaway. 
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
           inputbox.get_attribute('placeholder'),
           'Enter a to-do item'
        )

        # They type "Buy peacock feathers" into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When they hit enter, the page updates and now lists "1: Buy peacock feathers" 
        # as item in list. 
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        
        # Text box inviting them to add another item remains. 
        # They enter "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates and now shows both items on the list. 
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to makea  fly',
            [row.text for row in rows]
        )

        # Person sees that the site has generated a unique URL for them; 
        # this is accompanied by some explanatory text to that effect. 
        self.fail('Finish the test!')

        # They visit the URL and see their to-do list is still there. 

        # They exit the browser.

if __name__ == '__main__':
    unittest.main(warnings='ignore')