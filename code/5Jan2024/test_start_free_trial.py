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

    free_trial = driver.find_element(By.XPATH, "//a[text()='Start a free trial']")
    free_trial.click()

    time.sleep(10)

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage", "Invalid URL"

    close_btn = driver.find_element(By.XPATH, "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon' and @aria-label='Close']")
    close_btn.click()
