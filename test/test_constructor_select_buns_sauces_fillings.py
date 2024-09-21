import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from selenium.webdriver.support import expected_conditions as ec


class TestConstructor:
    dataset = [
        [[Locators.SAUCES, Locators.SAUCES_PARENT],
         [Locators.FILLINGS, Locators.FILLINGS_PARENT],
         [Locators.BUNS, Locators.BUNS_PARENT]]
    ]

    @pytest.mark.parametrize('dataset', dataset)
    def test_constructor_select_buns_sauces_fillings(self, driver, dataset):
        for locator, locator_parent in dataset:
            select_item = driver.find_element(*locator)
            select_item.click()

            # пробовал через WebDriverWait - не реагирует
            WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located(locator_parent))

            driver.implicitly_wait(3)  # оставил через implicitly_wait
            item_parent = driver.find_element(*locator_parent)
            assert 'current' in item_parent.get_attribute('class')
