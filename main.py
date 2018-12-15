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
    element = driver_instance.find_element_by_name("q")

    # Clear any prepopulated text in the input field
    element.clear()

    # Send keys and return at the end
    element.send_keys("Selenium is awesome!" + Keys.RETURN)

    # Assert that we don't have 'No results found' anywhere in the page source
    assert "No result found" not in driver_instance.page_source

    # Close the tab, not entire browser
    # driver_instance.close()


if __name__ == '__main__':
    seleniumTest()
