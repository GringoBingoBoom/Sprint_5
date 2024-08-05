import pytest
from selenium import webdriver
from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.URL)

    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    login_button = driver.find_element(*Locators.BUTTON_LOGIN_TO_ACCOUNT)
    login_button.click()

    WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.SIGN_IN_TITLE))

    input_register_name = driver.find_element(*Locators.INPUT_REGISTER_EMAIL)
    input_register_name.send_keys(Data.EMAIL)

    input_register_name = driver.find_element(*Locators.INPUT_REGISTER_PASSWORD)
    input_register_name.send_keys(Data.PASSWORD)

    register_button = driver.find_element(*Locators.BUTTON_SIGNIN)
    register_button.click()

    WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))
