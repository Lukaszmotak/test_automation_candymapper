from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[data-aid='CREATE_ACCOUNT_NAME_FIRST']")
    LAST_NAME = (By.CSS_SELECTOR, "input[data-aid='CREATE_ACCOUNT_NAME_LAST']")
    EMAIL = (By.CSS_SELECTOR, "input[data-aid='CREATE_ACCOUNT_EMAIL']")
    PHONE = (By.CSS_SELECTOR, "input[data-aid='CREATE_ACCOUNT_PHONE']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-ux-btn='primary']")


class CreateAccountPage(BasePage):

    def fill_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def fill_phone(self, phone):
        self.driver.find_element(*Locators.PHONE).send_keys(phone)

    def submit_create_account(self):
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

    def verify_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(Locators.FIRST_NAME))