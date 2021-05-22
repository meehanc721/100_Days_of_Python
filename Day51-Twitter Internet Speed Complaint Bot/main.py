import selenium, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException


PROMISED_DOWN = 200
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
GECKODRIVER_PATH = "C:\\Users\\meeha\\Desktop\\geckodriver\\geckodriver.exe"
TWITTER_USERNAME = "username"
TWITTER_PASSWORD = "**********"


class InternetSpeedTwitterBot():

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def find_element(self, xpath):
        found_element = False
        element = None
        while not found_element:
            try:
                element = self.driver.find_element_by_xpath(xpath)
                found_element = True
            except exceptions.NoSuchElementException or StaleElementReferenceException:
                found_element = False
        return element

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(2)
        go = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(40)

        self.down = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")

        print(f"Download Speed: {self.down.text} Mbps")
        print(f"Upload Speed: {self.up.text} Mbps")
        time.sleep(3)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()
        time.sleep(3)
        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")
        username.send_keys(TWITTER_USERNAME)
        password.send_keys(TWITTER_PASSWORD)
        password.submit()
        time.sleep(5)

        text_box = self.find_element(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )
        text_box.send_keys(f"Hey @Ask_Spectrum, why is my internet speed {self.down.text} down / {self.up.text} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up???")


        #tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
        # tweet_compose.click()
        # time.sleep(2)
        # textbox = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        #textbox.send_keys(f"Hey @Ask_Spectrum, why is my internet speed {self.down.text} down / {self.up.text} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up???")


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

bot.get_internet_speed()
bot.tweet_at_provider()

