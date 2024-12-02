import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.wildberries.ru/"


@allure.epic("QAP")
@allure.feature("Locators")
@allure.story("CSS")
class TestCSSLocators:
    @allure.title("Проверка нахождения элемента корзина")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_by_css_class(self, driver_chrome):
        """Ищем корзину"""
        driver = driver_chrome
        driver.get(url)
        elements = driver.find_elements(By.CSS_SELECTOR, '.navbar-pc__icon.navbar-pc__icon--basket')

        assert len(elements) == 1
        assert elements[0].is_displayed()

    @allure.title("Проверка нахождения элемета поисковой строки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_by_css_id(self, driver_chrome):
        """Ищем поисковую строчку"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.CSS_SELECTOR, '#searchInput')

        time.sleep(7)

        assert element.is_displayed()

        element.send_keys('джинсы')
        time.sleep(7)

        # проверка введеного текста
        assert element.get_attribute('value') == 'джинсы'

    @allure.title("Проверка нахождения лого")
    @allure.severity(allure.severity_level.NORMAL)
    def test_by_css_full_attribute(self, driver_chrome):
        """Ищем логотип"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.CSS_SELECTOR,
                                      'img[src="//static-basket-01.wbbasket.ru/vol2/site/i/v3/header/logo_2024_11_14.webp"]')

        time.sleep(7)
        assert element.is_displayed()

    @allure.title("Проверка нахождения элемета валюта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_by_css_attribute(self, driver_chrome):
        """Ищем валюту"""
        driver = driver_chrome
        driver.get(url)
        elements = driver.find_elements(By.CSS_SELECTOR, '[class="simple-menu__currency"]')

        time.sleep(7)
        assert elements[0].is_displayed()
        assert len(elements) == 1

    @allure.title("Проверка работы элемента button с навигайцией по сайту")
    @allure.severity(allure.severity_level.NORMAL)
    def test_by_css_class2(self, driver_chrome):
        """Ищем button c навигацией по сайту, затем кликаем и ищем другой элемент"""
        driver = driver_chrome
        driver.get(url)
        element = driver.find_element(By.CSS_SELECTOR, '.nav-element__burger-line')

        assert element.is_displayed()

        element.click()

        # Ожидаем появления другого элемента
        new_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.nav-element__burger.j-menu-burger-btn.j-wba-header-item.nav-element__burger--close')))

        assert new_element.is_displayed()