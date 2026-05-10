from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    EMAIL = (By.CSS_SELECTOR, "input[data-aid='MEMBERSHIP_SSO_LOGIN_EMAIL']")
    PASSWORD = (By.CSS_SELECTOR, "input[data-aid='MEMBERSHIP_SSO_LOGIN_PASSWORD']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-aid='MEMBERSHIP_SSO_SUBMIT']")


class SignInPage(BasePage):

    def fill_email(self, email):
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def submit_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()

    def verify_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(Locators.EMAIL))
