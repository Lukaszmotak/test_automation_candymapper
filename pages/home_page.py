from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators:

    CLOSE_POPUP = (By.ID, "popup-widget5912-close-icon")
    FIRST_NAME = (By.CSS_SELECTOR, "input[data-aid='First_Name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[data-aid='Last_Name']")
    EMAIL = (By.CSS_SELECTOR, "input[data-aid='CONTACT_FORM_EMAIL']")
    PHONE_NUMBER = (By.CSS_SELECTOR, "input[data-aid='By entering a Phone Number you agree to our SMS Terms of Service']")
    MESSAGE = (By.ID, "CONTACT_FORM_MESSAGE")
    USER_ICON = (By.CSS_SELECTOR, "[data-aid='MEMBERSHIP_ICON_DESKTOP_RENDERED']")
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/m/create-account']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "a[href='/m/account']")

class HomePage(BasePage):
    def close_popup(self):
        self.driver.find_element(*Locators.CLOSE_POPUP).click()

    def open_user_menu(self):
        self.driver.find_element(*Locators.USER_ICON).click()

    def go_to_sign_in(self):
        self.open_user_menu()
        self.driver.find_element(*Locators.SIGN_IN_LINK).click()

    def go_to_create_account(self):
        self.open_user_menu()
        self.driver.find_element(*Locators.CREATE_ACCOUNT_LINK).click()

    def verify_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(Locators.USER_ICON))