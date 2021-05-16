import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.get("http://secure-retreat-92358.herokuapp.com/")

# no_of_articles = driver.find_element_by_css_selector("#articlecount a")
# #no_of_articles.click()

# all_portals = driver.find_element_by_link_text("a bombing")
# all_portals.click()

# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Biggest Poo")
# search_bar.send_keys(Keys.ENTER)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Conor")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Meehan")

email = driver.find_element_by_name("email")
email.send_keys("codechad721@gmail.com")
email.submit()

