import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class TestPersonalAccount:
    dataset = [
        [Data.URL, Locators.CONSTRUCTOR, Locators.MAIN_PAGE_TITLE],
        [Data.URL, Locators.LOGO, Locators.MAIN_PAGE_TITLE],
        [Data.URL_LOGIN, Locators.BUTTON_EXIT, Locators.SIGN_IN_TITLE]
    ]

    def test_go_to_personal_account(self, driver, login):
        personal_account_button = driver.find_element(*Locators.PERSONAL_ACCOUNT)
        personal_account_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.PROFILE))

        assert driver.current_url == Data.URL_PROFILE

    @pytest.mark.parametrize('target_url, locator, locator_target', dataset)
    def test_from_personal_account_to_constructor_to_logo_to_exit(self, driver, login, target_url, locator,
                                                                  locator_target):
        personal_account_button = driver.find_element(*Locators.PERSONAL_ACCOUNT)
        personal_account_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.PROFILE))

        constructor_button = driver.find_element(*locator)
        constructor_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(locator_target))

        assert driver.current_url == target_url
