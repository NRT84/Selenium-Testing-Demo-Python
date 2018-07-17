from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Helpers import driver
import allure


class HomePage:

    def __init__(self):
        self.url = "https://www.python.org"

    def go_to(self):
        with allure.step("go to url: {0}".format(self.url)):
            driver.navigate(self.url)

    def search(self, text):
        with allure.step("search for {0}".format(text)):
            if not isinstance(text, str):
                raise TypeError("Url must be a string")
            self._search_box.send_keys(text)
            self._go_button.click()

    # region Web Elements
    @property
    def _search_box(self):
        identifier = "id-search-field"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _go_button(self):
        identifier = "submit"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)
    # endregion
