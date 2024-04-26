from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://sbis.ru/")
    sleep(1)
    header = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    header.click()
    sleep(1)
    header = driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    header.click()
    sleep(1)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    sleep(1)
    header = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    driver.execute_script("arguments[0].scrollIntoView();", header)
    sleep(1)
    header = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg [href="/about"]')
    header.click()
    sleep(1)
    assert driver.current_url == 'https://tensor.ru/about'
finally:
    driver.quit()
