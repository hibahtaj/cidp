import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.environ.get('BASE_URL', 'http://127.0.0.1:5055')

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(15)
    yield browser
    browser.quit()

def load_form(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'name')))

def test_empty_name(driver):
    load_form(driver)
    driver.find_element(By.ID, 'password').send_keys('testpassword')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.execute_script('return document.getElementById("name").validity.valueMissing')

def test_empty_password(driver):
    load_form(driver)
    driver.find_element(By.ID, 'name').send_keys('student')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.execute_script('return document.getElementById("password").validity.valueMissing')

def test_successful_registration(driver):
    load_form(driver)
    driver.find_element(By.ID, 'name').send_keys('Student')
    driver.find_element(By.ID, 'email').send_keys('student@example.com')
    driver.find_element(By.ID, 'password').send_keys('testpassword')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert 'Registration Successful!' in driver.page_source
    assert driver.find_element(By.ID, 'welcome').text == 'Welcome Student'
