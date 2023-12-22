"""Tests Example File."""

import pytest

from templates.templates import EXAMPLE_URL


@pytest.mark.skip()
class TestExample:

    def test_example(self, driver):
        """
        Method that navigates to the `EXAMPLE_URL` and verifies that the page URL matches the opened URL.

        Asserts:
            - Validates the URL of the Current Page.

        Args:
            driver (WebDriver): Selenium WebDriver instance.

        """
        driver.get(EXAMPLE_URL)
        assert driver.current_url == EXAMPLE_URL

        # Test example.
        # All tests in `tests` module should match the format of `test_example` function:
        #     - All tests start with the `test_` string.
        #     - All tests are grouped in Test Cases inside classes whose names starts with the `Test` string.
        #     - All tests have one or more assertions.
        #     - All tests docstring should be in Google docstring format.
