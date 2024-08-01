import pytest 

import allure 
from data import login_data
from pages.base.base_page import BasePage 
from pages.login.login import LoginPage
from pages.admin.system_users import SystemUsers
from pages.admin.system_users import SystemUsers 
from selenium import webdriver 

@pytest.mark.smoke
class TestAddUser:

    def setup_class(self):
        self.driver=webdriver.Firefox()
        self.base_page=BasePage(self.driver)
        self.login_page=LoginPage(self.driver)
        self.system_users=SystemUsers

    def test_login_with_super_admin(self):
        self.admin_page.visit()
        self.login_page.fillLogin_form(**login_data.super_admin_credential)
        assert self.base_page.is_element_visible(*self.login_page._welcome_button)
        self.base_page.wait_visibility_element(*self.system_users._admin_menu)

    def test_access_system_users_menu(self):
        self.system_users.access_system_users_menu()

    def teardown_class(self):
        self.driver.close()

