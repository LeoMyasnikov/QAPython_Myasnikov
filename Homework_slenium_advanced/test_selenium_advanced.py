import os.path
import time
import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


url_right_mouse_click = 'https://the-internet.herokuapp.com/context_menu'
url_keyboard_click = 'https://the-internet.herokuapp.com/key_presses'
url_js_click = 'https://the-internet.herokuapp.com/hovers'
url_text = 'https://the-internet.herokuapp.com/inputs'
url_alert = 'https://the-internet.herokuapp.com/javascript_alerts'
url_windows = 'https://the-internet.herokuapp.com/windows'
url_iframe = 'https://the-internet.herokuapp.com/iframe'
url_file_download = 'https://the-internet.herokuapp.com/download'
url_file_uplaod = 'https://the-internet.herokuapp.com/upload'


def test_mouse_click(driver_chrome):
    driver = driver_chrome
    driver.get(url_right_mouse_click)
    element = driver.find_element(By.ID, 'hot-spot')

    assert element.is_displayed()

    action = ActionChains(driver)
    action.context_click(element).perform()

    alert = driver.switch_to.alert
    time.sleep(5)
    assert alert.text == 'You selected a context menu'


def test_keyboard_click(driver_chrome):
    driver = driver_chrome
    driver.get(url_keyboard_click)
    element = driver.find_element(By.ID, 'target')

    assert element.is_displayed()

    action = ActionChains(driver)
    action.key_down(Keys.ESCAPE).perform()
    escape = driver.find_element(By.ID, 'result')

    assert escape.text == "You entered: ESCAPE"


def test_js_click(driver_chrome):
    driver = driver_chrome
    driver.get(url_js_click)
    element = driver.find_element(By.CSS_SELECTOR, "[href='/users/2']")
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(5)

    assert driver.title != 'The Internet'
    print("Элемент успешно кликнут с помощью JavaScript, cтраница обновилась")


def test_text(driver_chrome):
    driver = driver_chrome
    driver.get(url_text)
    element = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    element.send_keys('2157')

    assert element.get_attribute('value') == "2157"


def test_access_alert(driver_chrome):
    driver = driver_chrome
    driver.get(url_alert)
    button = driver.find_element(By.CSS_SELECTOR, '[onclick="jsAlert()"]')
    button.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()

    success = driver.find_element(By.ID, "result")
    assert success.text == "You successfully clicked an alert"


def test_dismiss_alert(driver_chrome):
    driver = driver_chrome
    driver.get(url_alert)
    button = driver.find_element(By.CSS_SELECTOR, '[onclick="jsConfirm()"]')
    button.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()

    cancel = driver.find_element(By.ID, "result")
    assert cancel.text == "You clicked: Cancel"


def test_sendkeys_alert(driver_chrome):
    driver = driver_chrome
    driver.get(url_alert)
    button = driver.find_element(By.CSS_SELECTOR, '[onclick="jsPrompt()"]')
    button.click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Ответ на запрос")
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Ответ на запрос"


def test_windows(driver_chrome):
    driver = driver_chrome
    driver.get(url_windows)
    button = driver.find_element(By.CSS_SELECTOR, '[href="/windows/new"]')
    button.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    time.sleep(5)
    assert driver.title == "New Window"


def test_iframe(driver_chrome):
    driver = driver_chrome
    driver.get(url_iframe)
    iframe = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(iframe)
    time.sleep(7)
    content = driver.find_element(By.XPATH, '//p')

    assert content.text == 'Your content goes here.'
    driver.switch_to.default_content()


def test_file_upload(driver_chrome):
    driver = driver_chrome
    driver.get(url_file_uplaod)
    file_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_path = 'C:/capture/htmlimage.png'
    file_element.send_keys(file_path)
    file_element.implicity_wait(5)
    upload_element = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    upload_element.click()
    message = driver.find_element(By.CSS_SELECTOR, 'h3')

    assert message.text == 'File Uploaded!'


def test_file_download(driver_chrome):
    driver = driver_chrome
    driver.get(url_file_download)
    file_element = driver.find_element(By.CSS_SELECTOR, 'a[href="download/Picture4.jpg"]')
    file_element.click()
    time.sleep(5)
    expected_file = os.path.join('C:/Users/lmyasnikov', "Picture4.jpg")

    assert os.path.exists(expected_file), f"Файл не найден: {expected_file}"
    print("Файл успешно скачан:", expected_file)