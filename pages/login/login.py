from pages.base.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
import time

class LoginPage(BasePage):
    _username_field=(By.ID,'txtUsername')
    _password_filed=(By.ID,'txtPassword')
    _login_buttom=(By.ID,'btnLogin')
    _welcome_button=(By.ID,'welcome')

    def __init__(self,driver):
        super().__init__(driver)

    def fillLogin_form(self,username,password):
        self.find_element(*self._username_field).send_keys(username)
        self.find_element(*self._password_filed).send_keys(password)
        self.find_element(*self._login_buttom).click()
        time.sleep(5)