from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import requests
from Helpers import driver
import allure


class NavigationBar:

    @allure.step("click the 'download' button")
    def downloads_button_go_to(self):
            self._downloads_button.click()

    @allure.step("validate that the 'downloads' button will yield the latest link")
    def validate_downloads_latest_link(self):
        url = self._download_latest_link.get_property("href")
        req = requests.get(url)
        assert req.status_code == 200

    @allure.step("validate that the 'about' button is present")
    def validate_about_button_is_present(self):
        assert self._about_button.is_displayed()

    @allure.step("validate that the 'downloads' button is present")
    def validate_downloads_button_is_present(self):
        assert self._downloads_button.is_displayed()

    @allure.step("validate that the 'documentation' button is present")
    def validate_documentation_button_is_present(self):
        assert self._documentation_button.is_displayed()

    @allure.step("validate that the 'community' button is present")
    def validate_community_button_is_present(self):
        assert self._community_button.is_displayed()

    @allure.step("validate that the 'stories' button is present")
    def validate_success_stories_button_is_present(self):
        assert self._success_stories_button.is_displayed()

    @allure.step("validate that the 'news' button is present")
    def validate_news_button_is_present(self):
        assert self._news_button.is_displayed()

    @allure.step("validate that the 'events' button is present")
    def validate_events_button_is_present(self):
        assert self._events_button.is_displayed()

    # region Web Elements
    @property
    def _about_button(self):
        identifier = "about"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _downloads_button(self):
        identifier = "downloads"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _documentation_button(self):
        identifier = "documentation"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _community_button(self):
        identifier = "community"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _success_stories_button(self):
        identifier = "success-stories"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _news_button(self):
        identifier = "news"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _events_button(self):
        identifier = "events"
        return driver.wait_for_element(By.ID, identifier, ec.visibility_of_element_located)

    @property
    def _download_latest_link(self):
        identifier = "//div[@class='header-banner ']//div[@class='download-os-source']//a[@class='button']"
        return driver.wait_for_element(By.XPATH, identifier, ec.visibility_of_element_located)
    # endregion
