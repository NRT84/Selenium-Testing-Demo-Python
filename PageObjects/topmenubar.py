from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Helpers import driver


class TopMenuBar:

    def validate_python_button_is_present(self):
        assert self._python_button.is_displayed()

    def validate_psf_button_is_present(self):
        assert self._psf_button.is_displayed()

    def validate_docs_button_is_present(self):
        assert self._docs_button.is_displayed()

    def validate_pypi_button_is_present(self):
        assert self._pypi_button.is_displayed()

    def validate_jobs_button_is_present(self):
        assert self._jobs_button.is_displayed()

    def validate_community_button_is_present(self):
        assert self._community_button.is_displayed()

    #region Web Elements
    @property
    def _python_button(self):
        identifier = "//ul[@class='menu']//a[@class='current_item selectedcurrent_branch selected']"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.XPATH, identifier)))
        return driver.instance.find_element_by_xpath(identifier)

    @property
    def _psf_button(self):
        identifier = "psf-meta "
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, identifier)))
        return driver.instance.find_element_by_class_name(identifier)

    @property
    def _docs_button(self):
        identifier = "docs-meta "
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, identifier)))
        return driver.instance.find_element_by_class_name(identifier)

    @property
    def _pypi_button(self):
        identifier = "pypi-meta "
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, identifier)))
        return driver.instance.find_element_by_class_name(identifier)

    @property
    def _jobs_button(self):
        identifier = "jobs-meta "
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, identifier)))
        return driver.instance.find_element_by_class_name(identifier)

    @property
    def _community_button(self):
        identifier = "shop-meta "
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.CLASS_NAME, identifier)))
        return driver.instance.find_element_by_class_name(identifier)
    #endregion
