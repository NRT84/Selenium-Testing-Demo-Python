from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os

_current_dir_path = os.path.dirname(os.path.abspath(__file__))
_driver_path = "{0}/../Drivers/geckodriver".format(_current_dir_path)
instance = webdriver.Firefox(executable_path=_driver_path)
instance.maximize_window()


def teardown():
    instance.quit()


def navigate(url):
    if not isinstance(url, str):
        raise TypeError("Url must be a string")
    instance.get(url)


def wait_for_element(by, identifier, cls_ec, timeout_in_seconds=5):
    WebDriverWait(instance, timeout_in_seconds).until(cls_ec((by, identifier)))
    return instance.find_element(by, identifier)
