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
    right_swipe_btn = driver.find_element(By.XPATH, "//div[@class='swiper-button-next']")
    right_swipe_btn.click()
    time.sleep(1)
    right_swipe_btn.click()
    time.sleep(1)
    right_swipe_btn.click()


def test_change_currency():
    currency_btn = driver.find_element(By.XPATH, "//button[@class='btn btn-link dropdown-toggle' and @data-toggle='dropdown']")
    gbp_btn = driver.find_element(By.XPATH, "//button[@class='currency-select btn btn-link btn-block' and @name='GBP']")
    action.click(currency_btn).click(gbp_btn).perform()


def test_desktop():
    desktop_dd = driver.find_element(By.XPATH, "//a[text()='Desktops']")
    mac_dd = driver.find_element(By.XPATH, "//a[text()='Mac (1)']")
    action.move_to_element(desktop_dd).click(mac_dd).perform()
    time.sleep(2)


def test_imac():
    imac_btn = driver.find_element(By.XPATH, "//a[text()='iMac']")
    action.key_down(Keys.CONTROL).click(imac_btn).perform()

    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)

    imac_img = driver.find_element(By.XPATH, "(//img[@title='iMac'])[1]")
    driver.execute_script("arguments[0].click();", imac_img)

    time.sleep(2)

    img_lbl = driver.find_element(By.XPATH, "//div[@class='mfp-counter']")
    assert img_lbl.text == '1 of 3'

    next_btn = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
    next_btn.click()
    assert img_lbl.text == '2 of 3'

    time.sleep(2)

    next_btn.click()
    assert img_lbl.text == '3 of 3'

    time.sleep(2)

    close_btn = driver.find_element(By.XPATH, "//button[@title='Close (Esc)' and @class='mfp-close']")
    close_btn.click()
