import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_login():
    LOGGER = logging.getLogger("__name__")
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    email_address_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys("Wingify@123")
    sign_in_button_ele.click()

    time.sleep(5)

    error_ele = driver.find_element(By.ID, "js-notification-box-msg")
    LOGGER.info(driver.title)
    assert error_ele.text == "Your email, password, IP address or location did not match", "Invalid error"
