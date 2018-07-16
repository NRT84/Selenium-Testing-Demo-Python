from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import requests
from Helpers import driver


class NavigationBar:

    def downloads_button_go_to(self):
        self._downloads_button.click()

    def validate_downloads_latest_link(self):
        url = self._download_latest_link.get_property("href")
        req = requests.get(url)
        assert req.status_code == 200

    def validate_about_button_is_present(self):
        assert self._about_button.is_displayed()

    def validate_downloads_button_is_present(self):
        assert self._downloads_button.is_displayed()

    def validate_documentation_button_is_present(self):
        assert self._documentation_button.is_displayed()

    def validate_community_button_is_present(self):
        assert self._community_button.is_displayed()

    def validate_success_stories_button_is_present(self):
        assert self._success_stories_button.is_displayed()

    def validate_news_button_is_present(self):
        assert self._news_button.is_displayed()

    def validate_events_button_is_present(self):
        assert self._events_button.is_displayed()

    # region Web Elements
    @property
    def _about_button(self):
        identifier = "about"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _downloads_button(self):
        identifier = "downloads"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _documentation_button(self):
        identifier = "documentation"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _community_button(self):
        identifier = "community"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _success_stories_button(self):
        identifier = "success-stories"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _news_button(self):
        identifier = "news"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _events_button(self):
        identifier = "events"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.ID, identifier)))
        return driver.instance.find_element_by_id(identifier)

    @property
    def _download_latest_link(self):
        identifier = "//div[@class='header-banner ']//div[@class='download-os-source']//a[@class='button']"
        WebDriverWait(driver.instance, driver.element_timeout).until(
            ec.visibility_of_element_located((By.XPATH, identifier)))
        return driver.instance.find_element_by_xpath(identifier)
    # endregion
