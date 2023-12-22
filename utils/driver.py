"""Tests WebDriver File."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from tests.config import *

BROWSER_OPTIONS = {
    "chrome": ChromeOptions(),
    "edge": EdgeOptions(),
}

BROWSER_PARAMS = [
    ("chrome", {}),
    ("chrome", {"deviceName": "iPad Air"}),
    ("chrome", {"deviceName": "iPhone 14 Pro Max"}),

    ("edge", {}),
    ("edge", {"deviceName": "iPad Air"}),
    ("edge", {"deviceName": "iPhone 14 Pro Max"}),
]


@pytest.fixture(params=BROWSER_PARAMS, scope="module")
def driver(request):
    """
    Fixture that provides a WebDriver instance based on specified browser parameters.

    Args:
        request: The Pytest fixture request object.

    """
    browser, mobile_emulation = request.param

    if browser not in BROWSER_OPTIONS:
        raise ValueError(
            f"The {browser} is not supported."
        )

    options = BROWSER_OPTIONS[browser]

    if BROWSER_INCOGNITO and browser == "chrome":
        options.add_argument("--incognito")

    if BROWSER_INCOGNITO and browser == "edge":
        options.add_argument("--inprivate")

    if BROWSER_NO_SANDBOX:
        options.add_argument("--no-sandbox")

    if BROWSER_HEADLESS:
        options.add_argument("--headless")

    if BROWSER_START_MAXIMIZED:
        options.add_argument("--start-maximized")

    if BROWSER_DISABLE_WEB_SECURITY:
        options.add_argument("--disable-web-security")

    if BROWSER_ACCEPT_INSECURE_CERTS:
        options.to_capabilities()["acceptInsecureCerts"] = True

    if mobile_emulation:
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = (
        webdriver.Chrome(options=options) if browser == "chrome" else
        webdriver.Edge(options=options) if browser == "edge" else None
    )

    yield driver
    driver.quit()
