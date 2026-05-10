import unittest
from selenium import webdriver
from pages.home_page import HomePage



class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://candymapper.com/")
        self.home_page = HomePage(self.driver)
        self.home_page._verify_page_loaded()


    def tearDown(self):
        self.driver.quit()
