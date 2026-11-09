
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = "http://127.0.0.1:5055"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

def test_page_title(driver):
    driver.get(URL)
    assert "Registration Form" in driver.page_source

def test_name_field(driver):
    driver.get(URL)
    name = driver.find_element(By.ID, "name")
    name.send_keys("Student")
    assert name.get_attribute("value") == "Student"
