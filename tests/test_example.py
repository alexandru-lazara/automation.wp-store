"""Tests Example File."""

from tests.templates.templates import EXAMPLE_URL


class TestExample:

    def test_example(self, driver):
        """
        This method navigates to the `EXAMPLE_URL` and verifies that the current page URL matches the expected URL.

        Args:
            driver (WebDriver): The WebDriver instance

        """
        driver.get(EXAMPLE_URL)
        assert driver.current_url == EXAMPLE_URL

        # Test example.
        # All tests in `tests` module should match the format of `test_example` function:
        #     - All tests start with the `test_` string.
        #     - All tests are grouped in Test Cases inside class whose name starts with the `Test` string.
        #     - All tests have one or more assertions.
        #     - All tests docstring should be in Google format.
