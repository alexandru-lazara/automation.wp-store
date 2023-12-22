"""Tests My Account Page and Customer Flows."""

import pytest
from selenium.webdriver.common.by import By

from templates.accounts import *
from templates.selectors import *
from templates.templates import *
from tests.conftest import go_to_page, wait_for_preloader_disappearance

TEST_CASES_CUSTOMER_LOGIN_INVALID = [
    *CUSTOMER_LOGIN_MISSING_CREDENTIALS,
    *CUSTOMER_LOGIN_INVALID_CREDENTIALS
]

TEST_CASES_CUSTOMER_LOGIN_VALID = [
    *CUSTOMER_LOGIN_VALID_CREDENTIALS
]

TEST_CASES_CUSTOMER_REGISTER_PASSWORD_STRENGTH = [
    *CUSTOMER_REGISTER_PASSWORD_STRENGTH
]


class TestMyAccount:

    def test_my_account_customer_login_elements_presence(self, driver):
        """
        Test that My Account Login Section elements are rendered into page.

        Asserts:
            - Validates the presence of Customer Login Section.
            - Validates the presence of Customer Login Section Heading and its value.
            - Validates the presence of Customer Login Section Username Label and its value.
            - Validates the presence of Customer Login Section Username Input Field.
            - Validates the presence of Customer Login Section Password Label and its value.
            - Validates the presence of Customer Login Section Password Input Field.
            - Validates the presence of Customer Login Section Remember Me Label and its value.
            - Validates the presence of Customer Login Section Remember Me Checkbox.
            - Validates the presence of Customer Login Section Log In Button and its value.
            - Validates the presence of Customer Login Section Lost Password Notice and its value.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, MY_ACCOUNT_HEADING)

        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_SECTION)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_HEADING).text == HEADING_LOGIN
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_LABEL).text == LABEL_USERNAME
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_LABEL).text == LABEL_PASSW0RD
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_INPUT)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_REMEMBER_ME_LABEL).text == LABEL_REMEMBER_ME
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_REMEMBER_ME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_LOG_IN_BUTTON).text == LABEL_LOG_IN
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_LOST_PASSWORD).text == LABEL_LOST_PASSW0RD

    def test_my_account_customer_register_elements_presence(self, driver):
        """
        Verifies and validates that Customer Register Section elements are rendering into page.

        Asserts:
            - Validates the presence of Customer Register Section.
            - Validates the presence of Customer Register Section Heading and its value.
            - Validates the presence of Customer Register Section Username Label and its value.
            - Validates the presence of Customer Register Section Username Input Field.
            - Validates the presence of Customer Register Section Password Label and its value.
            - Validates the presence of Customer Register Section Password Input Field.
            - Validates the presence of Customer Register Section Register Button and its value.
            - Validates the presence of Customer Register Section Privacy Policy and its value.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, MY_ACCOUNT_HEADING)

        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_SECTION)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_HEADING).text == HEADING_REGISTER
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_USERNAME_LABEL).text == LABEL_EMAIL
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_USERNAME_INPUT)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSW0RD_LABEL).text == LABEL_PASSW0RD
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSWORD_INPUT)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_BUTTON).text == HEADING_REGISTER
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PRIVACY_POLICY).text == LABEL_PRIVACY_POLICY


class TestMyAccountCustomerLogin:

    @pytest.mark.parametrize("account_data", TEST_CASES_CUSTOMER_LOGIN_INVALID)
    def test_my_account_customer_login_invalid(self, driver, account_data):
        """
        Test My Account Login with Invalid Account.

        Asserts:
            - Validates the displayed error message matches the expected error message.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            account_data (class): Dataclass containing customer account test data.

        """
        go_to_page(driver, MY_ACCOUNT_URL, MY_ACCOUNT_HEADING)

        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_INPUT).send_keys(account_data.username)
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_INPUT).send_keys(account_data.password)
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_LOG_IN_BUTTON).click()
        wait_for_preloader_disappearance(driver)

        assert driver.find_element(By.XPATH, XPATH_WOOCOMMERCE_ERROR_NOTICE).text == account_data.message_expect

    @pytest.mark.parametrize("account_data", TEST_CASES_CUSTOMER_LOGIN_VALID)
    def test_my_account_customer_login_valid(self, driver, account_data):
        """
        Test My Account Login with Valid Account.

        Asserts:
            - Validates the redirect

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            account_data (class): Dataclass containing customer account test data.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, MY_ACCOUNT_HEADING)

        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_USERNAME_INPUT).send_keys(account_data.username)
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_PASSW0RD_INPUT).send_keys(account_data.password)
        driver.find_element(By.XPATH, XPATH_CUSTOMER_LOGIN_LOG_IN_BUTTON).click()
        wait_for_preloader_disappearance(driver)

        assert driver.find_elements(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION)

        driver.find_element(By.XPATH, XPATH_MY_ACCOUNT_NAVIGATION_LINK_LOGOUT).click()
        wait_for_preloader_disappearance(driver)


class TestMyAccountCustomerRegister:

    @pytest.mark.parametrize("account_data", TEST_CASES_CUSTOMER_REGISTER_PASSWORD_STRENGTH)
    def test_my_account_customer_register_password(self, driver, account_data):
        """
        Method that validates My Account Customer Registration Password Strength.

        Asserts:
            - Validates the presence of Password Strength Info and its value.
            - Validates the presence of Password Hint Info based on Password Strength and its value.
            - Validates the presence of Customer Register Section Register Button (Disabled) and its value.
            - Validates the presence of Customer Register Section Register Button (Enabled) and its value.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            account_data (class): Dataclass containing customer account test data.

        """
        if driver.current_url != MY_ACCOUNT_URL:
            go_to_page(driver, MY_ACCOUNT_URL, MY_ACCOUNT_HEADING)

        driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSWORD_INPUT).clear()
        driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSWORD_INPUT).send_keys(account_data.password)
        assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSWORD_STRENGTH).text == \
               account_data.password_strength

        if account_data.password_strength in [PASSWORD_STRENGTH_VERY_WEAK, PASSWORD_STRENGTH_WEAK]:
            assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_PASSWORD_HINT).text == PASSWORD_HINT
            assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_BUTTON_DISABLED).text == HEADING_REGISTER
        if account_data.password_strength in [PASSWORD_STRENGTH_MEDIUM, PASSWORD_STRENGTH_STRONG]:
            assert driver.find_element(By.XPATH, XPATH_CUSTOMER_REGISTER_BUTTON).text == HEADING_REGISTER
