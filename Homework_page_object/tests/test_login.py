import time
import allure
from Homework_page_object.pages.login_page import loginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('LoginPage')
class TestLoginPage():

    def test_open_page(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.assert_page_is_opened()

    def test_login(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located(login_page.login_field))
        personal_page = login_page.enter_cridentionals()
        personal_page.assert_page_is_opened()

    def test_change_language(self, driver):
        login_page = loginPage(driver)
        login_page.open()
        login_page.change_language()






