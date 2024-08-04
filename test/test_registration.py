import random
import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestRegistration:

    dataset = [
        ["123456", Locators.SIGN_IN_TITLE],
        ["12345", Locators.ALARM_WRONG_PASSWORD]
    ]

    @pytest.mark.parametrize('password, locator', dataset)
    def test_registration_with_correct_and_less_then_6_string_password(self, driver, password, locator):
        login_button = driver.find_element(*Locators.BUTTON_LOGIN_TO_ACCOUNT)
        login_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.LINK_TO_REGISTER))

        register_link = driver.find_element(*Locators.LINK_TO_REGISTER)
        register_link.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.REGISTER_TITLE))

        input_register_name = driver.find_element(*Locators.INPUT_REGISTER_NAME)
        input_register_name.send_keys(Data.NAME)

        input_register_name = driver.find_element(*Locators.INPUT_REGISTER_EMAIL)
        input_register_name.send_keys(f'sergeyvelichko12{random.randint(100, 999)}@yandex.ru')

        input_register_name = driver.find_element(*Locators.INPUT_REGISTER_PASSWORD)
        input_register_name.send_keys(password)

        register_button = driver.find_element(*Locators.BUTTON_REGISTER)
        register_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(locator))

        assert driver.find_element(*locator).is_displayed()
