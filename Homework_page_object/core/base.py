import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_element(self, selector):
        return self.driver.find_element(*selector) # поскольку используется несколько типов локаторов, то передаем selector

    def fill_login_crieds(self, selector, login):
        element = self.get_element(selector)
        element.send_keys(login)

    def fill_password_crieds(self, selector, password):
        element = self.get_element(selector)
        element.send_keys(password)

    def click_on(self, selector):
        element = self.get_element(selector)
        element.click()

    def force_click_on(self, selector):
        element = self.get_element(selector)
        self.driver.execute_script("arguments[0].click();", element)






