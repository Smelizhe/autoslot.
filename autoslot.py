from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import chromedriver_binary
driver = webdriver.Chrome()
import time
p1="img/cat5.jpg"
url = "https://hosimiya7.github.io/slotgame/"
driver.get(url)
element0 = driver.find_element_by_id("stop0")
element1 = driver.find_element_by_id("stop1")
element2 = driver.find_element_by_id("stop2")
reset = driver.find_element_by_id("reset")
while True:
    for i in range(3):
        time.sleep(1)
        element0.click()
        time.sleep(3)
        element1.click()
        time.sleep(2.5)
        element2.click()
