from pages.base.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SystemUsers(BasePage):
    _admin_menu=(By.LINK_TEXT,'Admin')
    _user_management_menu = (By.ID,'menu_admin_UserManagement')

    _add_user_button= (By.ID,'btnAdd')
    _user_role_dropdown=(By.ID,'systemUser_userType')
    _employee_name_field=(By.ID,'systemUser_employeeName_empName')
    _user_name_field=(By.ID,'systemUser_userName')
    _status_dropdown = (By.ID, 'systemUser_status')
    _password_field=(By.ID,'systemUser_password')
    _confirm_password_field=(By.ID,'systemUser_confirmPassword')


    def __init__(self,driver):
        super().__init__(driver)

    def access_system_users_menu(self):
        self.find_element(*self._admin_menu).click()

    def createNewUser(self,user_role,employee_name,username,status,password,confirm_password):
        self.select_option(*self._user_role_dropdown,user_role)
        self.find_element(*self._employee_name_field,employee_name)
        self.select_option(*self._status_dropdown,status)
        self.find_element(*self._employee_name_field).send_keys(username)
        self.find_element(*self._password_field).send_keys(password)
        self.find_element(*self._confirm_password_field).send_keys(confirm_password)
