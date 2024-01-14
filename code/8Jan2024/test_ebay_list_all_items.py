import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options)


def test_open_webpage():
    driver.get("https://www.ebay.com/")


def test_ebay_search_items():
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box.send_keys("16 gb")

    category = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select a category for search']"))
    category.select_by_visible_text("Computers/Tablets & Networking")

    search_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
    search_btn.click()


def test_list_items():
    item_list = driver.find_elements(By.XPATH, "//span[@role='heading']")
    # item_list[2].click()
    for i in item_list:
        if "Dell" in i.text:
            i.click()
            break
