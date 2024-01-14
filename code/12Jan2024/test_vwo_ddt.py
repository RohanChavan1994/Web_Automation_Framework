import logging
import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_vwo_login():
    LOGGER = logging.getLogger(__name__)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")

    testdata = []
    workbook = openpyxl.load_workbook(
        r"C:\Users\Lenovo\PycharmProjects\Web_Automation_Framework\src\resources\testdata\test_vwo_ddt_testdata.xlsx")
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        testdata.append(f"{username}")
        testdata.append(f"{password}")
    username = testdata[0]
    password = testdata[1]

    email_address_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_address_ele.send_keys(username)

    password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password_ele.send_keys(password)

    checkbox_ele = driver.find_element(By.XPATH, "(//*[local-name()='svg' and @class='checkbox-radio-icon' and @icon-name='icon--checkbox-button'])[1]")
    checkbox_ele.click()

    sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    sign_in_button_ele.click()

    WebDriverWait(driver, 10, poll_frequency=1).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//div//h1[text()='Dashboard']"), "Dashboard"))

    LOGGER.info(driver.title)
    assert driver.title == "Dashboard", "Invalid page"

    dash_name = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding' and @data-qa='lufexuloga']")
    LOGGER.info(dash_name.text)

    assert dash_name.text == "Aman", "Invalid name"
