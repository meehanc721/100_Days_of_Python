import selenium, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

GECKODRIVER_PATH = "C:\\Users\\meeha\\Desktop\\geckodriver\\geckodriver.exe"

# Set the Firefox profile settings
profile = webdriver.FirefoxProfile("C:\\Users\\meeha\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\xhf8yuhr.default-release-1621276768820")
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference("useAutomationExtension", False)
profile.set_preference("geo.enabled", True)
profile.set_preference("geo.provider.use_corelocation", True)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(executable_path=GECKODRIVER_PATH, firefox_profile=profile, desired_capabilities=desired)

driver.get("https://tinder.com/")

# Hit Login
time.sleep(2)
page_links = driver.find_elements_by_tag_name("a")
login = page_links[9]
time.sleep(3)
login.click()

# Choose Google
time.sleep(5)
buttons = driver.find_elements_by_tag_name("button")
google = buttons[6]
google.click()

time.sleep(20)

# Allow location
allow_location = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]/span")
time.sleep(2)
allow_location.click()

# hit Not Interested
time.sleep(5)
not_interested = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]/span")
not_interested.click()


out_of_likes = 0
while out_of_likes != 100:
    try:
        like = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button")
        time.sleep(2)
        like.click()
        out_of_likes += 1
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            time.sleep(2)
            no_thanks = driver.find_element_by_xpath("/html/body/div[2]/div/div/button[2]/span")
            no_thanks.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()

