import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class TestPersonalAccount:
    dataset = [
        ["https://stellarburgers.nomoreparties.site/", Locators.CONSTRUCTOR],
        ["https://stellarburgers.nomoreparties.site/", Locators.LOGO],
        ["https://stellarburgers.nomoreparties.site/login", Locators.BUTTON_EXIT]
    ]

    def test_go_to_personal_account(self, driver, login):
        personal_account_button = driver.find_element(*Locators.PERSONAL_ACCOUNT)
        personal_account_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.PROFILE))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    @pytest.mark.parametrize('target_url, locator', dataset)
    def test_from_personal_account_to_constructor_to_logo_to_exit(self, driver, login, target_url, locator):
        personal_account_button = driver.find_element(*Locators.PERSONAL_ACCOUNT)
        personal_account_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(Locators.PROFILE))

        constructor_button = driver.find_element(*locator)
        constructor_button.click()

        time.sleep(3)

        assert driver.current_url == target_url
