import pytest
from Helpers import pages, driver


class TestsSmoke:

    @pytest.fixture(autouse=True)
    def setup(self):
        pages.home_page.go_to()

    @pytest.fixture(scope="module", autouse=True)
    def teardown(self):
        yield
        driver.teardown()

    def test_elements_visible_on_top_menu_bar(self):
        pages.top_menu_bar.validate_python_button_is_present()
        pages.top_menu_bar.validate_psf_button_is_present()
        pages.top_menu_bar.validate_docs_button_is_present()
        pages.top_menu_bar.validate_pypi_button_is_present()
        pages.top_menu_bar.validate_jobs_button_is_present()
        pages.top_menu_bar.validate_community_button_is_present()

    def test_elements_visible_on_navigation_bar(self):
        pages.navigation_bar.validate_about_button_is_present()
        pages.navigation_bar.validate_downloads_button_is_present()
        pages.navigation_bar.validate_documentation_button_is_present()
        pages.navigation_bar.validate_community_button_is_present()
        pages.navigation_bar.validate_success_stories_button_is_present()
        pages.navigation_bar.validate_news_button_is_present()
        pages.navigation_bar.validate_events_button_is_present()

    def test_validate_download_link(self):
        pages.navigation_bar.downloads_button_go_to()
        pages.navigation_bar.validate_downloads_latest_link()
