"""Tests Accounts File."""

from templates.templates import *
from utils.dataclasses import AccountData

# ### test_my_account.py ############################################
# ###################################################################

NONEXISTENT_USER = {
    "EMAIL": "test@example.com",
    "USERNAME": "test",
    "PASSWORD": "test"
}

VALID_USER = {
    "EMAIL": "user@example.com",
    "USERNAME": "user",
    "PASSWORD": "user"
}

VALID_ADMIN = {
    "EMAIL": "admin@example.com",
    "USERNAME": "admin",
    "PASSWORD": "admin"
}

REGISTER_CUSTOMER_PASSWORD_VERY_WEAK = {
    "PASSWORD": "abcd"
}

REGISTER_CUSTOMER_PASSWORD_WEAK = {
    "PASSWORD": "strength"
}

REGISTER_CUSTOMER_PASSWORD_MEDIUM = {
    "PASSWORD": "strength!1234"
}

REGISTER_CUSTOMER_PASSWORD_STRONG = {
    "PASSWORD": "strength!1234#TEST"
}


CUSTOMER_LOGIN_MISSING_CREDENTIALS = [
    AccountData(
        username=EMPTY_STRING,
        password=VALID_USER["PASSWORD"],
        message_expect=MISSING_USERNAME_ERROR),

    AccountData(
        username=VALID_USER["EMAIL"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR),

    AccountData(
        username=VALID_USER["USERNAME"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR),

    AccountData(
        username=NONEXISTENT_USER["EMAIL"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR),

    AccountData(
        username=NONEXISTENT_USER["USERNAME"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR),

    AccountData(
        username=EMPTY_STRING,
        password=EMPTY_STRING,
        message_expect=MISSING_USERNAME_ERROR)
]

CUSTOMER_LOGIN_INVALID_CREDENTIALS = [
    AccountData(
        username=NONEXISTENT_USER["EMAIL"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=UNKNOWN_EMAIL_ERROR),

    AccountData(
        username=NONEXISTENT_USER["USERNAME"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_USERNAME_ERROR.format(NONEXISTENT_USER["PASSWORD"])),

    AccountData(
        username=VALID_USER["EMAIL"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_EMAIL_PASSWORD_ERROR.format(VALID_USER["EMAIL"])),

    AccountData(
        username=VALID_USER["USERNAME"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_USERNAME_PASSWORD_ERROR.format(VALID_USER["USERNAME"]))
]

CUSTOMER_LOGIN_VALID_CREDENTIALS = [
    AccountData(
        username=VALID_USER["EMAIL"],
        password=VALID_USER["PASSWORD"]),

    AccountData(
        username=VALID_USER["USERNAME"],
        password=VALID_USER["PASSWORD"]),

    AccountData(
        username=VALID_ADMIN["USERNAME"],
        password=VALID_ADMIN["PASSWORD"]),

    AccountData(
        username=VALID_ADMIN["USERNAME"],
        password=VALID_ADMIN["PASSWORD"])
]

CUSTOMER_REGISTER_PASSWORD_STRENGTH = [
    AccountData(
        password=REGISTER_CUSTOMER_PASSWORD_VERY_WEAK["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_VERY_WEAK),

    AccountData(
        password=REGISTER_CUSTOMER_PASSWORD_WEAK["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_WEAK),

    AccountData(
        password=REGISTER_CUSTOMER_PASSWORD_MEDIUM["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_MEDIUM),

    AccountData(
        password=REGISTER_CUSTOMER_PASSWORD_STRONG["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_STRONG),
]
