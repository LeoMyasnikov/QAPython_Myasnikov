import allure
import time
from Homework_page_object.pages.login_page import loginPage

@allure.feature('PersonalPage')
class TestScanningPage():

    def test_open_scanning_page(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        time.sleep(7)
        scanning_page.assert_scanning_page_is_opened()

    def test_project_choice(self, driver):
        login_page = loginPage(driver)
        login_page.open_scanning()
        scanning_page = login_page.login_in_scanning()
        scanning_page.project_choice()
        time.sleep(7)
        scanning_page.assert_current_url()


