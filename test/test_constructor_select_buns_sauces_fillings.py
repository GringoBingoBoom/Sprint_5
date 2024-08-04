import time
import pytest
from locators import Locators
from selenium.webdriver.common.by import By


class TestConstructor:
    dataset = [
        [Locators.SAUCES,
         Locators.FILLINGS,
         Locators.BUNS]
    ]

    @pytest.mark.parametrize('dataset', dataset)
    def test_constructor_select_buns_sauces_fillings(self, driver, dataset):
        for locator in dataset:
            select_item = driver.find_element(*locator)
            select_item.click()

            time.sleep(3)

            item_parent = select_item.find_element(By.XPATH, '..')

            assert 'current' in item_parent.get_attribute('class')
