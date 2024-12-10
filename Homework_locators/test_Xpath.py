import time
import allure
from selenium.webdriver.common.by import By


url = "https://www.wildberries.ru/"


@allure.epic("QAP")
@allure.feature("Locators")
@allure.story("XPATH")
class TestXpathLocators:
    def test_by_xpath_class(self, driver_chrome):
        """Ищем корзину"""
        driver = driver_chrome
        driver.get(url)
        elements = driver.find_elements(By.XPATH, '//*[@class="navbar-pc__icon navbar-pc__icon--basket"]')

        assert len(elements) == 1
        assert elements[0].is_displayed()

    def test_by_xpath_id(self, driver_chrome):
        """Ищем поисковую строчку"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*[@id="searchInput"]')

        time.sleep(5)
        assert element.is_displayed()

        element.send_keys('джинсы')
        time.sleep(5)

        assert element.get_attribute('value') == 'джинсы'  # проверка введеного текста

    def test_by_xpath_full_attribute(self, driver_chrome):
        """Ищем логотип"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.XPATH,
                                      '//img[@src="//static-basket-01.wbbasket.ru/vol2/site/i/v3/header/logo_2024_11_14.webp"]')

        time.sleep(7)
        assert element.is_displayed()

    def test_by_xpath_of_part_attribute(self, driver_chrome):
        """Ищем валюту"""
        driver = driver_chrome
        driver.get(url)
        elements = driver.find_elements(By.XPATH,
                                        '//span[contains(@class,"__currency")]')

        time.sleep(7)
        assert elements[0].is_displayed()
        assert len(elements) == 1

    def test_by_xpath_class2(self, driver_chrome):
        """Ищем button c навигацией по сайту, затем кликаем и ищем другой элемент"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.XPATH, '//span[@class="nav-element__burger-line"]')

        time.sleep(5)
        assert element.is_displayed()

        element.click()

        time.sleep(5)
        new_elements = driver.find_elements(By.XPATH,
                                            '//button[@class="nav-element__burger j-menu-burger-btn j-wba-header-item nav-element__burger--close"]')

        assert new_elements[0].is_displayed()
        assert len(new_elements) == 1