# Automate the Cookie Clicker game
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")

timeout = time.time() + 60*5
print(time.strftime("%H:%M:%S", time.localtime()))
while True:
    cookie.click()
    try:
        active_product = driver.find_element_by_css_selector("#products .enabled")
        active_product.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    try:
        active_upgrade = driver.find_element_by_css_selector("#upgrades .enabled")
        active_upgrade.click()
    except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.StaleElementReferenceException) as e:
        pass
    if time.time() > timeout:
        try:
            # a div within the (div id =cookies)
            print(f"cookies {driver.find_element_by_css_selector('#cookies div').text}")
            print(time.strftime("%H:%M:%S", time.localtime()))
            break
        except selenium.common.exceptions.StaleElementReferenceException:
            pass
driver.quit()


