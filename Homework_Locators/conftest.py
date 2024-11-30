import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def driver_firefox():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "C:/Users/lmyasnikov/",  # Установка директории загрузки
        "download.prompt_for_download": False,  # Отключение запроса на подтверждение загрузки
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.quit()