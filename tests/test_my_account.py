"""Tests My Account Page."""

import pytest
from selenium.webdriver.common.by import By

from templates.accounts import *
from templates.selectors import *
from templates.templates import *
from tests.conftest import (assert_my_account_navigation_link, go_to_page,
                            wait_for_preloader_disappearance)

TEST_CASES_MY_ACCOUNT_LOGIN = [
    *MY_ACCOUNT_LOGIN_MISSING_CREDENTIALS,
    *MY_ACCOUNT_LOGIN_INVALID_CREDENTIALS,
    *MY_ACCOUNT_LOGIN_VALID_CREDENTIALS
]
TEST_CASES_MY_ACCOUNT_ACCESS_WP_ADMIN_DASHBOARD = [
    *MY_ACCOUNT_ACCESS_WP_ADMIN_DASHBOARD
]
TEST_CASES_MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH = [
    *MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH
]


class TestMyAccountLogin:

    def test_my_account_login_elements_presence(self, driver):
        """
        Verifies and Validates that My Account Login Section elements are rendered into page.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, HEADING_MY_ACCOUNT)

        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_SECTION)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_HEADING).text == HEADING_LOGIN
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_USERNAME_LABEL).text == LABEL_LOGIN_USERNAME
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_USERNAME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_LABEL).text == LABEL_LOGIN_PASSW0RD
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_INPUT)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_REMEMBER_ME_LABEL).text == LABEL_LOGIN_REMEMBER_ME
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_REMEMBER_ME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_LOG_IN_BUTTON).text == LABEL_LOGIN_BUTTON
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_LOST_PASSWORD).text == LABEL_LOGIN_LOST_PASSW0RD

    @pytest.mark.usefixtures("my_account_logout_scope_function")
    @pytest.mark.parametrize("my_account_data", TEST_CASES_MY_ACCOUNT_LOGIN)
    def test_my_account_login(self, driver, my_account_data):
        """
        Verifies and Validates My Account Login Functionality.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            my_account_data (class): Dataclass containing customer account test data.

        """
        go_to_page(driver, MY_ACCOUNT_URL, HEADING_MY_ACCOUNT)

        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_USERNAME_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_USERNAME_INPUT).send_keys(my_account_data.username)
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_INPUT).send_keys(my_account_data.password)

        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_LOGIN_LOG_IN_BUTTON).click()
        wait_for_preloader_disappearance(driver)

        if my_account_data in [
            *MY_ACCOUNT_LOGIN_MISSING_CREDENTIALS,
            *MY_ACCOUNT_LOGIN_INVALID_CREDENTIALS
        ]:
            assert driver.find_element(By.XPATH, XPATH_NOTICES_WRAPPER_ERROR).text == my_account_data.message_expect

        elif my_account_data in [
            *MY_ACCOUNT_LOGIN_VALID_CREDENTIALS
        ]:
            assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION)

    @pytest.mark.usefixtures("my_account_login_scope_function")
    @pytest.mark.usefixtures("my_account_logout_scope_function")
    @pytest.mark.parametrize("my_account_data", TEST_CASES_MY_ACCOUNT_ACCESS_WP_ADMIN_DASHBOARD)
    def test_my_account_access_wp_admin_dashboard(self, driver, my_account_data):
        """
        Verifies and Validates My Account Access to WordPress Admin Dashboard.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            my_account_data (class): Dataclass containing customer account test data.

        """
        driver.get(WP_ADMIN_DASHBOARD)
        assert my_account_data.admin_redirect_url in driver.current_url


class TestMyAccountRegister:

    def test_my_account_register_elements_presence(self, driver):
        """
        Verifies and validates that Customer Register Section elements are rendering into page.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, HEADING_MY_ACCOUNT)

        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_SECTION)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_HEADING).text == HEADING_REGISTER
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_USERNAME_LABEL).text == LABEL_REGISTER_EMAIL
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_USERNAME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSW0RD_LABEL).text == LABEL_REGISTER_PASSW0RD
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSWORD_INPUT)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_BUTTON).text == HEADING_REGISTER
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PRIVACY_POLICY).text == \
               LABEL_REGISTER_PRIVACY_POLICY

    @pytest.mark.parametrize("my_account_data", TEST_CASES_MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH)
    def test_my_account_register_password_strength(self, driver, my_account_data):
        """
        Verifies and Validates My Account Register Password Strength.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            my_account_data (class): Dataclass containing customer account test data.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, HEADING_MY_ACCOUNT)

        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSWORD_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSWORD_INPUT).send_keys(my_account_data.password)
        assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH).text == \
               my_account_data.password_strength

        if my_account_data.password_strength in [
            PASSWORD_STRENGTH_VERY_WEAK,
            PASSWORD_STRENGTH_WEAK
        ]:
            assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_PASSWORD_HINT).text == PASSWORD_HINT
            assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_BUTTON_DISABLED).text == HEADING_REGISTER

        elif my_account_data.password_strength in [
            PASSWORD_STRENGTH_MEDIUM,
            PASSWORD_STRENGTH_STRONG
        ]:
            assert driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_REGISTER_BUTTON).text == HEADING_REGISTER


@pytest.mark.usefixtures("my_account_login_scope_class")
@pytest.mark.parametrize("my_account_login_scope_class", [MY_ACCOUNT_LOGIN_VALID_CREDENTIALS[0]], indirect=True)
class TestMyAccountNavigationLinks:

    def test_my_account_navigation_dashboard(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Dashboard.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        current_url = driver.current_url
        if current_url != MY_ACCOUNT_URL:
            driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_DASHBOARD.format(status=NOT_ACTIVE)).click()
            wait_for_preloader_disappearance(driver)

        assert_my_account_navigation_link(driver, status_dashboard=IS_ACTIVE)
        assert driver.current_url == MY_ACCOUNT_URL
        assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_MY_ACCOUNT

    def test_my_account_navigation_orders(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Orders.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_ORDERS.format(status=NOT_ACTIVE)).click()
        wait_for_preloader_disappearance(driver)

        assert_my_account_navigation_link(driver, status_orders=IS_ACTIVE)
        assert driver.current_url == MY_ACCOUNT_ORDERS_URL
        assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_ORDERS

    def test_my_account_navigation_downloads(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Downloads.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_DOWNLOADS.format(status=NOT_ACTIVE)).click()
        wait_for_preloader_disappearance(driver)

        assert_my_account_navigation_link(driver, status_downloads=IS_ACTIVE)
        assert driver.current_url == MY_ACCOUNT_DOWNLOADS_URL
        assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_DOWNLOADS

    def test_my_account_navigation_addresses(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Addresses.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ADDRESS.format(status=NOT_ACTIVE)).click()
        wait_for_preloader_disappearance(driver)

        assert_my_account_navigation_link(driver, status_edit_address=IS_ACTIVE)
        assert driver.current_url == MY_ACCOUNT_EDIT_ADDRESSES_URL
        assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_ADDRESSES

    def test_my_account_navigation_details(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Account Details.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ACCOUNT.format(status=NOT_ACTIVE)).click()
        wait_for_preloader_disappearance(driver)

        assert_my_account_navigation_link(driver, status_edit_account=IS_ACTIVE)
        assert driver.current_url == MY_ACCOUNT_EDIT_ACCOUNT_URL
        assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_ACCOUNT_DETAILS

    def test_my_account_navigation_logout(self, driver):
        """
        Verifies and validates the functionality of My Account Navigation for Logout.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        if MY_ACCOUNT_URL not in driver.current_url:
            go_to_page(driver, MY_ACCOUNT_URL, HEADING_MY_ACCOUNT)
        wait_for_preloader_disappearance(driver)

        current_url = driver.current_url
        if current_url == MY_ACCOUNT_URL:
            assert_my_account_navigation_link(driver, status_dashboard=IS_ACTIVE)
        else:
            endpoint = [x for x in current_url.replace("-", "_").split("/") if x != ""][-1]
            assert_my_account_navigation_link(driver, **{f"status_{endpoint}": IS_ACTIVE})

        if len(driver.find_elements(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION)) == 1:
            driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_LOGOUT).click()
            wait_for_preloader_disappearance(driver)

            assert driver.current_url == MY_ACCOUNT_URL
            assert driver.find_element(By.XPATH, XPATH_PAGE_HEADING).text == HEADING_MY_ACCOUNT
            TestMyAccountLogin().test_my_account_login_elements_presence(driver)
            TestMyAccountRegister().test_my_account_register_elements_presence(driver)
