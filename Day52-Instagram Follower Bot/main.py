import selenium, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
from pprint import pprint

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "username"
PASSWORD = "**********"

class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.submit()
        time.sleep(2)

        all_buttons = self.driver.find_elements_by_tag_name("button")
        not_now = all_buttons[1]
        not_now.click()
        time.sleep(2)

        not_now_again = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        not_now_again.click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(2)
        followers = self.driver.find_element_by_partial_link_text("followers")
        followers.click()
        time.sleep(2)

        # Scroll to reveal all the followers
        followers = self.driver.find_element_by_css_selector(".isgrP")
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(2)



    def follow(self):
        all_follow_buttons = self.driver.find_elements_by_css_selector("li div div button")
        for button in all_follow_buttons:
            try:
                button.click()
                time.sleep(600)
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        
bot = InstaFollower(CHROME_DRIVER_PATH)

bot.login()
bot.find_followers()
bot.follow()