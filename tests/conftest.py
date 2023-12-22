"""Tests Shared Functions File."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from templates.selectors import (STYLE_DISPLAY_NONE,
                                 XPATH_KENTA_PRELOADER_PRESET_3)
from tests.config import WEBDRIVER_TIMEOUT_SECONDS

pytest_plugins = [
    "utils.driver",
    "utils.logger",
]


def wait_for_preloader_disappearance(driver):
    """
    Wait for preloader to disappear.

    Args:
        driver (WebDriver): Selenium WebDriver instance.

    """
    WebDriverWait(driver, WEBDRIVER_TIMEOUT_SECONDS).until(
        ec.presence_of_element_located((By.XPATH, f"//{XPATH_KENTA_PRELOADER_PRESET_3}{STYLE_DISPLAY_NONE}")))


def go_to_page(driver, page_url, page_heading):
    """
    Navigate to the specified page URL, and validates that the page is the intended one.

    Asserts:
        - Validates the URL of the Current Page.
        - Validates the heading of the Current Page.
        - Validates the presence of Content Section.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        page_url (str): The URL of the page.
        page_heading (str): The heading of the page.

    """
    driver.get(page_url)
    wait_for_preloader_disappearance(driver)

    assert driver.current_url == page_url
    assert driver.find_element(By.XPATH, "//div[@class='card-content flex-grow']/div/h6").text == page_heading
    assert driver.find_element(By.ID, "content")
