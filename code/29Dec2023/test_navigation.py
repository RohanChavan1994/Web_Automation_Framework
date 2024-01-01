import time

from selenium import webdriver


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    driver.refresh()
    print(driver.title)
    driver.get("https://www.google.co.in")
    print(driver.title)
    driver.back()
    print(driver.title)
    driver.forward()
    print(driver.title)
    time.sleep(5)
