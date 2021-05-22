from bs4 import BeautifulSoup
import requests
from pprint import pprint
import selenium, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException


URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
FORM_LINK = "https://forms.gle/kASdoVCPdQKAC9rC8"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"



response = requests.get(URL,
                        headers={
                            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9"
                        })
zillow_web_page = response.text
soup = BeautifulSoup(zillow_web_page, "html.parser")

listing_links = soup.select(".list-card-top a")
all_links = []
for link in listing_links:
    href = link["href"]
    if "https" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

listing_addresses = soup.select(".list-card-addr")
all_addresses = [address.text.split(" | ")[-1]  for address in listing_addresses]

listing_prices = soup.select(".list-card-price")
all_prices = [price.text.split("+")[0] for price in listing_prices if "$" in price.text]



driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.maximize_window()

driver.get(FORM_LINK)
time.sleep(2)

all_inputs = driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput")
address_entry = all_inputs[0]
price_entry = all_inputs[1]
link_entry = all_inputs[2]
submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

for i in range(len(all_links)):
    all_inputs = driver.find_elements_by_css_selector(".quantumWizTextinputPaperinputInput")
    address_entry = all_inputs[0]
    price_entry = all_inputs[1]
    link_entry = all_inputs[2]
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    address_entry.send_keys(all_addresses[i])
    price_entry.send_keys(all_prices[i])
    link_entry.send_keys(all_links[i])
    submit.click()
    time.sleep(1)
    another = driver.find_element_by_link_text("Submit another response")
    another.click()
    time.sleep(5)



