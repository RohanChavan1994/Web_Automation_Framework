import logging
import pytest
from selenium import webdriver


def test_lab01():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    driver.maximize_window()
    print(driver.title)
    driver.close()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver


def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)

    driver.get("https://app.vwo.com")
    LOGGER.info(driver.title)

    # Assertions
    assert driver.title == "Login - VWO", "Invalid title"
