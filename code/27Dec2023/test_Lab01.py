from selenium import webdriver


def test_lab01():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    driver.maximize_window()
    print(driver.title)
    driver.close()
