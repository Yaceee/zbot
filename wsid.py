from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


url = "https://widget.weezevent.com/ticket/E1098393/?color_primary=0032FA&amp;locale=fr-fr&amp;width_auto=1&amp;o=minisite_v2&amp;code=64869&amp;neo=1"

def getWsid():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1 + random.random())
    element = driver.find_element(By.NAME, "wsid").get_attribute('value')

    return element

if __name__ == "__main__":
    print(getWsid())