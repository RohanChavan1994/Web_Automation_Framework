import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_login():
    LOGGER = logging.getLogger(__name__)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")

    email_address_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")

    password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password_ele.send_keys("ATBx@1234")

    sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in_button_ele.click()

    time.sleep(10)

    LOGGER.info(driver.title)
    assert driver.title == "Dashboard", "Invalid page"

    dash_name = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding' and @data-qa='lufexuloga']")
    LOGGER.info(dash_name.text)

    assert dash_name.text == "Aman", "Invalid name"
