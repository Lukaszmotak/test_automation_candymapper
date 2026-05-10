from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def verify_page_loaded(self):
        raise NotImplementedError("Each page must implement verify_page_loaded()")