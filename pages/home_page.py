from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:

    CLOSE_POPUP = (By.ID, "popup-widget5912-close-icon")
    FIRST_NAME = (By.CSS_SELECTOR, "input[data-aid='First_Name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[data-aid='Last_Name']")
    EMAIL = (By.CSS_SELECTOR, "input[data-aid='CONTACT_FORM_EMAIL']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[data-aid='By entering a Phone Number you agree to our SMS Terms of Service']")
    MESSAGE = (By.ID, "CONTACT_FORM_MESSAGE")

class HomePage(BasePage):
    def close_popup(self):
        self.driver.find_element(*Locators.CLOSE_POPUP).click()