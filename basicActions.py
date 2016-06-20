from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


#driver = webdriver.Chrome()
#driver.get("https://duckduckgo.com/")
#driver.quit()

class BrowseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://duckduckgo.com/")

    def test_Browse(self):
        driver=self.driver
        searchFieldXPath = ".//*[@id='sb_form_q']"
        searchButtonXPath = ".//*[@id='search_button_homepage']"

        searchFieldElement = WebDriverWait(driver, 10).until( driver.find_element_by_xpath(searchFieldXPath))
        searchButtonElement = WebDriverWait(driver, 10).until(driver.find_element_by_xpath(searchButtonXPath))

        searchFieldElement.clear()
        searchFieldElement.send_keys("Test String")
        searchButtonElement.click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
