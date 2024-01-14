import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwo_login():
    LOGGER = logging.getLogger("__name__")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")

    email_address_ele = driver.find_element(By.ID, "login-username")
    email_address_ele.send_keys("93npu2yyb0@esiix.com")

    password_ele = driver.find_element(By.NAME, "password")
    password_ele.send_keys("Wingify@123")

    checkbox_ele = driver.find_elements(By.XPATH, "//*[local-name()='svg' and @class='checkbox-radio-icon' and @icon-name='icon--checkbox-button']")
    #checkbox_ele = driver.find_element(By.XPATH, "//input[@name='password' and @id='login-password' and @data-qa='jobodapuxe']/following::div[2]/input[@type='checkbox' and @id='checkbox-remember' and @data-qa='fakiqedudu']")
    checkbox_ele[0].click()

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")
    sign_in_button_ele.click()

    time.sleep(5)

    error_ele = driver.find_element(By.ID, "js-notification-box-msg")
    LOGGER.info(driver.title)
    assert error_ele.text == "Your email, password, IP address or location did not match", "Invalid error"
