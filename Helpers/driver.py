from selenium import webdriver
import os

_current_dir_path = os.path.dirname(os.path.abspath(__file__))
_driver_path = "{0}/../Drivers/geckodriver".format(_current_dir_path)
element_timeout = 5
instance = webdriver.Firefox(executable_path=_driver_path)
instance.maximize_window()


def teardown():
    instance.quit()


def navigate(url):
    if not isinstance(url, str):
        raise TypeError("Url must be a string")
    instance.get(url)
