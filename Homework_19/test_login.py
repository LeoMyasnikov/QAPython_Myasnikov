from selenium.webdriver.common.by import By

url = 'https://demo.applitools.com/#'


def test_login_chrome(driver_chrome):
    """Тест авторизации на сайте Applitools Demo в Chrome."""
    driver = driver_chrome
    driver.get(url)

    
    # Заполнение формы авторизации
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "log-in").click()

    assert "ACME demo app" in driver.title


def test_login_firefox(driver_firefox):
    """Тест авторизации на сайте Applitools Demo в Firefox."""
    driver = driver_firefox
    driver.get(url)

    # Заполнение формы авторизации
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "log-in").click()

    assert "ACME demo app" in driver.title
