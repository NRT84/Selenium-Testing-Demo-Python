from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Helpers import driver
import allure


class TopMenuBar:

    @allure.step("validate that the 'python' button is present")
    def validate_python_button_is_present(self):
        assert self._python_button.is_displayed()

    @allure.step("validate that the 'psf' button is present")
    def validate_psf_button_is_present(self):
        assert self._psf_button.is_displayed()

    @allure.step("validate that the 'docs' button is present")
    def validate_docs_button_is_present(self):
        assert self._docs_button.is_displayed()

    @allure.step("validate that the 'pypi' button is present")
    def validate_pypi_button_is_present(self):
        assert self._pypi_button.is_displayed()

    @allure.step("validate that the 'jobs' button is present")
    def validate_jobs_button_is_present(self):
        assert self._jobs_button.is_displayed()

    @allure.step("validate that the 'community' button is present")
    def validate_community_button_is_present(self):
        assert self._community_button.is_displayed()

    # region Web Elements
    @property
    def _python_button(self):
        identifier = "//ul[@class='menu']//a[@class='current_item selectedcurrent_branch selected']"
        return driver.wait_for_element(By.XPATH, identifier, ec.visibility_of_element_located)

    @property
    def _psf_button(self):
        identifier = "psf-meta "
        return driver.wait_for_element(By.CLASS_NAME, identifier, ec.visibility_of_element_located)

    @property
    def _docs_button(self):
        identifier = "docs-meta "
        return driver.wait_for_element(By.CLASS_NAME, identifier, ec.visibility_of_element_located)

    @property
    def _pypi_button(self):
        identifier = "pypi-meta "
        return driver.wait_for_element(By.CLASS_NAME, identifier, ec.visibility_of_element_located)

    @property
    def _jobs_button(self):
        identifier = "jobs-meta "
        return driver.wait_for_element(By.CLASS_NAME, identifier, ec.visibility_of_element_located)

    @property
    def _community_button(self):
        identifier = "shop-meta "
        return driver.wait_for_element(By.CLASS_NAME, identifier, ec.visibility_of_element_located)
    # endregion
