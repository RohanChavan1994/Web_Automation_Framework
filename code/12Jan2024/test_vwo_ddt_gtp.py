import logging
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class ExcelReadError(Exception):
    pass


def read_excel_file():
    # Define the relative path to the Excel file
    excel_file_path = os.path.abspath("test_vwo_ddt_testdata.xlsx")

    try:
        df = pd.read_excel(excel_file_path)
        return df.to_dict(orient='list')
    except FileNotFoundError:
        raise ExcelReadError(f"File '{excel_file_path}' not found.")
    except Exception as e:
        raise ExcelReadError(f"Error reading Excel file: {e}")


def get_value(column_name, row_number, default=None):
    # Read the Excel file
    testdata = read_excel_file()

    if testdata is None:
        # Handle the case where reading the Excel file failed
        raise ExcelReadError("Unable to read Excel file.")

    # Fetch the value based on the provided column name and row number
    try:
        value = testdata[column_name][row_number - 1]
        return value
    except KeyError:
        print(f"Column '{column_name}' not found.")
    except IndexError:
        print(f"Row {row_number} not found.")
    return default


def test_vwo_login():
    LOGGER = logging.getLogger(__name__)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)

    try:
        driver.get("https://app.vwo.com")

        # Fetch values from the Excel file
        email_address_ele = driver.find_element(By.XPATH, "//input[@id='login-username']")
        email_address_ele.send_keys(get_value("username", 1))

        password_ele = driver.find_element(By.XPATH, "//input[@id='login-password']")
        password_ele.send_keys(get_value("password", 1))

        sign_in_button_ele = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
        sign_in_button_ele.click()

        time.sleep(10)

        LOGGER.info(driver.title)
        assert driver.title == get_value("title", 1), "Invalid page"

        dash_name = driver.find_element(By.XPATH, "//span[@class='Fw(semi-bold) ng-binding' and @data-qa='lufexuloga']")
        LOGGER.info(dash_name.text)

        assert dash_name.text == get_value("firstname", 1), "Invalid name"

    except ExcelReadError as e:
        LOGGER.error(str(e))
    finally:
        # Close the WebDriver in a finally block to ensure cleanup
        driver.quit()

# Rest of your code...
