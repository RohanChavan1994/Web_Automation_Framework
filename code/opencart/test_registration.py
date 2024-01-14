import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
action = ActionChains(driver)


def test_open_webpage():
    driver.get("https://awesomeqa.com/ui/")
    assert driver.title == "Your Store"


def test_navigate_registration_page():
    my_account_btn = driver.find_element(By.XPATH, "//a[@title='My Account']/span[text()='My Account']")
    register_btn = driver.find_element(By.XPATH, "//a[text()='Register']")

    action.click(my_account_btn).click(register_btn).perform()

    time.sleep(2)

    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/register"
    assert driver.title == "Register Account"


def test_user_registration():
    pass
