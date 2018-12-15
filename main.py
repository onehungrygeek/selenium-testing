# Library imports
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def seleniumTest():
    """
    Selenium test for creating browser instance and searching a query

    Returns:
        None -- None
    """

    # Disable the testing infobar
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")

    # Provide path for chromedriver
    chromedriver = os.getcwd() + "/chromedriver"

    # Create a driver instance with above chrome_options and
    # provide executable chromedriver path for the browser
    driver_instance = webdriver.Chrome(chromedriver,
                                       chrome_options=chrome_options)

    # Open a link in the browser
    driver_instance.get('https://www.google.com/')

    # Assert that the tab title will contain 'Google'
    assert "Google" in driver_instance.title

    # Find element named 'q' (You can find any element name by inspecting a page source)
    search_field = driver_instance.find_element_by_name("q")

    # Clear any prepopulated text in the input field
    search_field.clear()

    # Send keys and return at the end
    search_field.send_keys("Selenium is awesome!" + Keys.RETURN)

    # Assert that we don't have 'No results found' anywhere in the page source
    assert "No result found" not in driver_instance.page_source

    # Close the tab, not entire browser
    # driver_instance.close()


class GoogleTestCase(unittest.TestCase):
    """
    Simple unit testing module
    """

    def setUp(self):
        """
        Set up the browser instance with chromedriver and chrome_options
        """

        self.chromedriver = os.getcwd() + "/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-infobars")
        self.driver_instance = webdriver.Chrome(self.chromedriver,
                                                chrome_options=self.chrome_options)
        self.addCleanup(self.driver_instance.close)

    def testPageTitle(self):
        """
        Test page title in above browser instance
        """

        self.driver_instance.get('http://www.google.com')
        self.assertIn('Google', self.driver_instance.title)


if __name__ == '__main__':
    seleniumTest()
    unittest.main(verbosity=2)
