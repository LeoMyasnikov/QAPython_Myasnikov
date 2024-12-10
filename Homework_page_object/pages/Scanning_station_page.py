import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Homework_page_object.core.base import Base
from Homework_page_object.data.credentials import DOMAIN


class ScanningPage(Base):

    scanning_page = (By.XPATH, '//div[@class="modalTitle__VuTxy"]')
    choice_project = (By.XPATH, '//div[@class="selectTitle__OmThc"]')
    postgre_project = (By.XPATH, '//div[@class="selectOption__ablSb"]')
    expected_project_url = 'http://myasnikovhost/ContentCapture/Scanning/Batches?projectId=2'
    button_project_entrance = (By.XPATH, '//div/button[@class="button__z74UG buttonPrimary__EvbyJ"]')

    def __init__(self, driver):
        self.driver: WebDriver = driver

        self.page = f'{DOMAIN}Scanning/' # добавка к основному урлу ведущая на персональную страницу

    @allure.step('Assert scanning page is open')
    def assert_scanning_page_is_opened(self):
       assert self.get_element(self.scanning_page), 'Element is not visible'

    @allure.step('Выбор определенного проекта')
    def project_choice(self):
        self.click_on(self.choice_project)
        self.click_on(self.postgre_project)
        self.click_on(self.button_project_entrance)

    @allure.step('Проверка, что после выбора проекта открылась страница с нужным проектом')
    def assert_current_url(self):
        current_url = self.driver.current_url
        if current_url == self.expected_project_url:
            print("URL соответствует ожидаемому:", current_url)
        else:
            print("URL не соответствует. Ожидался:", self.expected_project_url, "Получен:", current_url)








