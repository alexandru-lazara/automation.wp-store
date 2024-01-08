"""Tests Logger File."""

import logging
import os
import time

import pytest


@pytest.fixture(autouse=True, scope="session")
def logger():
    """
    Fixture that provides a logging instance.

    Returns:
        logging.Logger: The logging instance.

    """
    return logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def _log_test_case_name(logger):
    """
    Fixture that logs the name of the current test case.

    Args:
        logger: The logging instance.

    """
    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    logger.info("TEST CASE")
    logger.info("%s.", test_name)


@pytest.fixture(autouse=True)
def _log_test_case_duration(logger):
    """
    Fixture that logs the duration of the current test case (in seconds) at the end of the test case.

    Args:
        logger: The logging instance.

    """
    test_start = time.time()

    yield
    logger.info("Test Case duration: \t %.2f seconds.", time.time() - test_start)
    logger.info("")


@pytest.fixture(autouse=True, scope="session")
def _log_test_suite_duration(logger):
    """
    Fixture that logs the duration of the test suite (in seconds) at the end of the test suite.

    Args:
        logger: The logging instance.

    """
    logger.info("Testing started...")
    logger.info("")
    test_start = time.time()

    yield
    logger.info("")
    logger.info("Test Suite duration: \t %.2f seconds.", time.time() - test_start)
