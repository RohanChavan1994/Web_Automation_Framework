import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def read_excel_file(file_path):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='list')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


def get_value(data, column_name, row_number):
    # Fetch the value based on the provided column name and row number
    try:
        value = data[column_name][row_number - 1]
        return value
    except KeyError:
        print(f"Column '{column_name}' not found.")
    except IndexError:
        print(f"Row {row_number} not found.")


def test_vwo_login():
    try:
        LOGGER = logging.getLogger(__name__)

        # Define the relative path to the Excel file
        excel_file_path = r".\src\resources\testdata\test_vwo_ddt_testdata.xlsx"

        print(excel_file_path)

        # Read the Excel file
        testdata = read_excel_file(excel_file_path)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(chrome_options)
        driver.get("https://app.vwo.com")

        # Fetch values from the Excel file
        email_address_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
        email_address_ele.send_keys(get_value(testdata, "username", 1))

        password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
        password_ele.send_keys(get_value(testdata, "password", 1))

        sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
        sign_in_button_ele.click()

        time.sleep(10)

        LOGGER.info(driver.title)
        assert driver.title == get_value(testdata, "title", 1), "Invalid page"

        dash_name = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding' and @data-qa='lufexuloga']")
        LOGGER.info(dash_name.text)

        assert dash_name.text == get_value(testdata, "firstname", 1), "Invalid name"

        # Rest of your test logic
    except Exception as error:
        print("Error occurred: ", error)
