from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.maximize_window()
driver.get("https://www.python.org")


#price = driver.find_element_by_id("priceblock_ourprice")
#print(price.text)

# Using name stores the value of what you enter when the form is submitted.
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# submit_bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events ={}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)


driver.quit()