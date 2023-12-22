"""Tests Logger File."""

import logging
import os
import time

import pytest


@pytest.fixture(autouse=True)
def logger():
    """
    Fixture that provides a logging instance.

    Returns:
        logging.Logger: The logging instance.

    """
    return logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def _log_test_name(logger):
    """
    Fixture that logs the name of the current test.

    Args:
        logger: The logging instance.

    """
    test_name = os.environ.get('PYTEST_CURRENT_TEST')
    logger.info("[TEST NAME\t\t] %s.", test_name)


@pytest.fixture(autouse=True)
def _log_test_duration_function(logger):
    """
    Fixture that logs the duration of the current test in seconds at the end of the test.

    Args:
        logger: The logging instance.

    """
    test_start = time.time()
    yield
    test_finish = time.time()
    logger.info("[TEST DURATION\t] %s seconds.", round(test_finish - test_start, 2))
