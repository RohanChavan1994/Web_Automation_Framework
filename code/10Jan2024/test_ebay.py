from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
action = ActionChains(driver)


def test_open_ebay():
    driver.get("https://www.ebay.com/")

    electronic = driver.find_element(By.XPATH, "//li[@class='vl-flyout-nav__js-tab']//a[text()='Electronics']")
    computer = driver.find_element(By.XPATH, "//a[text()='Computers and tablets']")
    action.move_to_element(electronic).click(computer).perform()


def test_click_laptop():
    WebDriverWait(driver, 10,poll_frequency=1).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//a//div[text()='PC Laptops']"), "PC Laptops"))

    pc_laptop = driver.find_element(By.XPATH, "//a//div[text()='PC Laptops']")
    pc_laptop.click()


def test_click_gb16():
    WebDriverWait(driver, 10, poll_frequency=1).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//a//p[text()='16 GB']"), "16 GB"))

    gb16 = driver.find_element(By.XPATH, "//a//p[text()='16 GB']")
    gb16.click()


def test_print_item_prices():
    WebDriverWait(driver, 10, poll_frequency=1).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a//h3[@class='s-item__title']")))

    item_name = driver.find_elements(By.XPATH, "//a//h3[@class='s-item__title']")
    item_price = driver.find_elements(By.XPATH, "//div//span[@class='s-item__price']")

    for name, price in zip(item_name, item_price):
        print(f"Name: {name.text} -> Price: {price.text}")

    driver.quit()
