import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui
from pprint import pprint

ACCOUNT_USERNAME = "_my_username"
ACCOUNT_PASSWORD = "my_password"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Hide automation from Chromium, open in maximized window
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--start-maximized")

driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&geoId=90000070&keywords=python%20developer&location=New%20York%20City%20Metropolitan%20Area")

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

#Email + Password
time.sleep(2)
login = driver.find_element_by_name("session_key")
login.send_keys(ACCOUNT_USERNAME)

login = driver.find_element_by_name("session_password")
login.send_keys(ACCOUNT_PASSWORD)
login.submit()

time.sleep(15)

# Remember button on browser
time.sleep(2)
remember = driver.find_element_by_class_name("btn__primary--large")
remember.click()

time.sleep(2)
all_listings = driver.find_elements_by_class_name("jobs-search-results__list-item")

for i in range(len(all_listings)):
    all_listings[i].click()
    time.sleep(3)

    try:
        # Easy Apply button
        time.sleep(3)
        apply = driver.find_element_by_class_name("jobs-apply-button--top-card")
        apply.click()

        # Submit
        submit_button = driver.find_element_by_css_selector("footer div button")

        if submit_button.get_attribute("data-control-name") == "submit_unify":
            # Enter number
            time.sleep(2)
            phone_number = driver.find_element_by_tag_name(".display-flex input")
            if phone_number == "":
                phone_number.send_keys("7029349088")
            else:
                continue

            # Unfollow company
            unfollow = driver.find_element_by_css_selector("div form footer div label").click()

            #Submit
            time.sleep(1)
            submit_button.click()
            time.sleep(3)

            # Once application completed, close the pop-up window.
            close_button = driver.find_element_by_tag_name("button")
            close_button.click()
        else:
            print("skip")
            close_button = driver.find_element_by_tag_name("button")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")



    except NoSuchElementException:
        print("No application button, skipped.")
        continue

















# # Choose option for Language dropdown question
# dropdown = driver.find_element_by_class_name("fb-dropdown")
# dropdown.click()
# for i in range(4):
#     pyautogui.press("down")



# unfollow company
unfollow = driver.find_element_by_xpath('//*[@id="ember349"]/div/div[2]/footer/div[1]/label').click()

# # Submit
# submit_application = driver.find_elements_by_tag_name("button")[5]
# submit_application.click()



