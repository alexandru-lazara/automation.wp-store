"""Tests Shared Functions File."""

import pytest
from _pytest.fixtures import FixtureLookupError
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from templates.selectors import (STYLE_DISPLAY_NONE,
                                 XPATH_KENTA_PRELOADER_PRESET_3,
                                 XPATH_MY_ACCOUNT_NAVIGATION,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_DASHBOARD,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_DOWNLOADS,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ACCOUNT,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ADDRESS,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_LOGOUT,
                                 XPATH_MY_ACCOUNT_NAVIGATION_LINK_ORDERS)
from templates.templates import (LABEL_ACCOUNT_DETAILS, LABEL_ADDRESSES,
                                 LABEL_DASHBOARD, LABEL_DOWNLOADS,
                                 LABEL_LOGOUT, LABEL_ORDERS, NOT_ACTIVE)
from tests.config import WEBDRIVER_TIMEOUT_SECONDS

pytest_plugins = [
    "utils.driver",
    "utils.logger",
]


# ### WordPress My Account - Login ##################################
# ###################################################################

def my_account_login(driver, request):
    """
    Perform Login on My Account Section.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        request: The Pytest fixture request object.

    """
    from tests.test_my_account import TestMyAccountLogin

    try:
        my_account_data = request.getfixturevalue('my_account_data')
    except FixtureLookupError:
        my_account_data = request.param

    if my_account_data.username and my_account_data.password:
        TestMyAccountLogin().test_my_account_login(driver, my_account_data)


@pytest.fixture()
def my_account_login_scope_function(driver, request):
    """
    Fixture that performs Login on My Account Section, within function scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        request: The Pytest fixture request object.

    """
    return my_account_login(driver, request)


@pytest.fixture(scope="class")
def my_account_login_scope_class(driver, request):
    """
    Fixture that performs Login on My Account Section, within class scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        request: The Pytest fixture request object.

    """
    return my_account_login(driver, request)


@pytest.fixture(scope="module")
def my_account_login_scope_module(driver, request):
    """
    Fixture that performs Login on My Account Section, within module scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        request: The Pytest fixture request object.

    """
    return my_account_login(driver, request)


# ### WordPress My Account - Logout #################################
# ###################################################################

def my_account_logout(driver, my_account_data):
    """
    Perform Logout from My Account Section.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        my_account_data (class): Dataclass containing customer account test data.

    """
    from tests.test_my_account import TestMyAccountNavigationLinks

    if my_account_data.username and my_account_data.password:
        TestMyAccountNavigationLinks().test_my_account_navigation_logout(driver)


@pytest.fixture()
def my_account_logout_scope_function(driver, my_account_data):
    """
    Fixture that performs Logout from My Account Section, within function scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        my_account_data (class): Dataclass containing customer account test data.

    """
    yield
    return my_account_logout(driver, my_account_data)


@pytest.fixture(scope="class")
def my_account_logout_scope_class(driver, my_account_data):
    """
    Fixture that performs Logout from My Account Section, within class scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        my_account_data (class): Dataclass containing customer account test data.

    """
    yield
    return my_account_logout(driver, my_account_data)


@pytest.fixture(scope="module")
def my_account_logout_scope_module(driver, my_account_data):
    """
    Fixture that performs Logout from My Account Section, within module scope.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        my_account_data (class): Dataclass containing customer account test data.

    """
    yield
    return my_account_logout(driver, my_account_data)


# ### Other functions ###############################################
# ###################################################################

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


def assert_my_account_navigation_link(
        driver,
        status_dashboard=NOT_ACTIVE,
        status_orders=NOT_ACTIVE,
        status_downloads=NOT_ACTIVE,
        status_edit_address=NOT_ACTIVE,
        status_edit_account=NOT_ACTIVE
):
    """
    Assert the presence and visibility of My Account Navigation Links.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        status_dashboard (str): My Account Navigation Link Dashboard Status -> 'ACTIVE' or 'NOT_ACTIVE'.
        status_orders (str): My Account Navigation Link Orders Status -> 'ACTIVE' or 'NOT_ACTIVE'.
        status_downloads (str): My Account Navigation Link Downloads Status -> 'ACTIVE' or 'NOT_ACTIVE'.
        status_edit_address (str): My Account Navigation Link Edit Address Status -> 'ACTIVE' or 'NOT_ACTIVE'.
        status_edit_account (str): My Account Navigation Link Edit Account Status -> 'ACTIVE' or 'NOT_ACTIVE'.

    """
    my_account_navigation_link_elements_list = [
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_DASHBOARD.format(status=status_dashboard), LABEL_DASHBOARD),
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_ORDERS.format(status=status_orders), LABEL_ORDERS),
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_DOWNLOADS.format(status=status_downloads), LABEL_DOWNLOADS),
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ADDRESS.format(status=status_edit_address), LABEL_ADDRESSES),
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ACCOUNT.format(status=status_edit_account), LABEL_ACCOUNT_DETAILS),
        (XPATH_MY_ACCOUNT_NAVIGATION_LINK_LOGOUT, LABEL_LOGOUT)
    ]

    if driver.find_elements(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION):
        for xpath, label in my_account_navigation_link_elements_list:
            assert driver.find_element(By.XPATH, xpath)
            assert driver.find_element(By.XPATH, xpath).text == label
