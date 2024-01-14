import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options)


def test_open_webpage():
    driver.get("https://katalon-demo-cura.herokuapp.com/")


def test_click_make_appointment_btn():
    assert driver.title == "CURA Healthcare Service", "Invalid title"

    make_appointment_btn_ele = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    make_appointment_btn_ele.click()


def test_login():
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Invalid URL"

    username_ele = driver.find_element(By.XPATH, "//input[@id='txt-username']")
    username_ele.send_keys("John Doe")

    password_ele = driver.find_element(By.XPATH, "//input[@id='txt-password']")
    password_ele.send_keys("ThisIsNotAPassword")

    login_btn_ele = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    login_btn_ele.click()


def test_create_appointment():
    # driver.switch_to.alert.accept()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Invalid URL"

    facility_ele = Select(driver.find_element(By.XPATH, "//select[@id='combo_facility']"))
    facility_ele.select_by_visible_text("Seoul CURA Healthcare Center")

    readmission_ele = driver.find_element(By.XPATH, "//input[@id='chk_hospotal_readmission']")
    readmission_ele.click()

    assert readmission_ele.get_attribute("checked"), "Checkbox is not checked"

    healthcare_program = driver.find_element(By.XPATH, "//input[@id='radio_program_medicaid']")
    healthcare_program.click()

    visit_date = driver.find_element(By.XPATH, "//input[@id='txt_visit_date']")
    visit_date.send_keys("01/01/2024")

    comments = driver.find_element(By.XPATH, "//textarea[@id='txt_comment']")
    comments.send_keys("test")

    book_appointment_btn = driver.find_element(By.XPATH, "//button[@id='btn-book-appointment']")
    book_appointment_btn.click()


def test_verify_appointment_details():

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary", "Invalid URL"

    lbl_facility = driver.find_element(By.XPATH, "//p[@id='facility']")
    assert lbl_facility.text == "Seoul CURA Healthcare Center"

    lbl_hospital_readmission = driver.find_element(By.XPATH, "//p[@id='hospital_readmission']")
    assert lbl_hospital_readmission.text == "Yes"

    lbl_program = driver.find_element(By.XPATH, "//p[@id='program']")
    assert lbl_program.text == "Medicaid"

    lbl_visit_date = driver.find_element(By.XPATH, "//p[@id='visit_date']")
    assert lbl_visit_date.text == "01/01/2024"

    lbl_comment = driver.find_element(By.XPATH, "//p[@id='comment']")
    assert lbl_comment.text == "test"

    options_ele = driver.find_element(By.XPATH, "//i[@class='fa fa-bars']")
    options_ele.click()

    home_link_ele = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
    home_link_ele.click()
