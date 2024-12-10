import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Homework_page_object.core.base import Base
from Homework_page_object.data.credentials import DOMAIN
from Homework_page_object.pages.Personal_page import PersonalPage
from Homework_page_object.pages.Scanning_station_page import ScanningPage


class loginPage(Base):

    login_page = (By.XPATH, '//div[@class="modalDialog__dialogTitle"]')
    login_field = (By.ID, 'userName')
    password_field = (By.ID, 'password')
    button_entrance = (By.CSS_SELECTOR, '[value="Войти"]')
    login = 'admin'
    password = 'password'
    language_hover = (By.XPATH, "//a[text()='English']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}Login/#/Login' # добавка к основному урлу ведущая на персональную страницу

        self.page_scanning = f'{DOMAIN}Scanning/'

    @allure.step('Open "Login" page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Open "Scanning" page')
    def open_scanning(self):
        self.driver.get(self.page_scanning)

    @allure.step('Assert this page is open')
    def assert_page_is_opened(self):
       element = self.get_element(self.login_page)
       assert element.is_displayed(), f"Element {self.login_page} is not visible"

    @allure.step('Authorization')
    def enter_cridentionals(self):
        self.fill_login_crieds(self.login_field, self.login)
        self.fill_password_crieds(self.password_field, self.password)
        self.click_on(self.button_entrance)
        personal_page = PersonalPage(self.driver)
        return personal_page

    @allure.step('Login with redirect in scanning station')
    def login_in_scanning(self):
        self.fill_login_crieds(self.login_field, self.login)
        self.fill_password_crieds(self.password_field, self.password)
        self.click_on(self.button_entrance)
        scanning_page = ScanningPage(self.driver)
        return scanning_page

    @allure.step('Сhange language')
    def change_language(self):
        self.force_click_on(self.language_hover)
        time.sleep(7)
        assert self.driver.title == 'Log In to ContentCapture'














