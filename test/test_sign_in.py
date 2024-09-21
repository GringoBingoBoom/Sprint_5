import pytest
from data import Data
from locators import Locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestSignIn:
    dataset = [
        [Data.URL, Locators.BUTTON_LOGIN_TO_ACCOUNT],
        [Data.URL, Locators.PERSONAL_ACCOUNT],
        [Data.URL_REGISTER, Locators.BUTTON_SIGNIN_ON_REGISTER_PAGE],
        [Data.URL_FORGOT_PASSWORD, Locators.BUTTON_SIGNIN_ON_REGISTER_PAGE]
    ]

    @pytest.mark.parametrize('url, locator', dataset)
    def test_signin_on_4_different_page(self, driver, url, locator):
        driver = webdriver.Chrome()
        driver.get(url)

        login_button = driver.find_element(*locator)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.SIGN_IN_TITLE))

        input_register_name = driver.find_element(*Locators.INPUT_REGISTER_EMAIL)
        input_register_name.send_keys(Data.EMAIL)

        input_register_name = driver.find_element(*Locators.INPUT_REGISTER_PASSWORD)
        input_register_name.send_keys(Data.PASSWORD)

        register_button = driver.find_element(*Locators.BUTTON_SIGNIN)
        register_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

        assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed()
