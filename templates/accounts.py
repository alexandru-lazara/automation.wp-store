"""Tests Accounts File."""

from templates.templates import *
from utils.dataclasses import AccountData

# ### test_my_account.py ############################################
# ######################################################################

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

MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_VERY_WEAK = {
    "PASSWORD": "str"
}
MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_WEAK = {
    "PASSWORD": "strength"
}
MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_MEDIUM = {
    "PASSWORD": "strength!1234"
}
MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_STRONG = {
    "PASSWORD": "strength!1234#TEST"
}

MY_ACCOUNT_LOGIN_MISSING_CREDENTIALS = [
    AccountData(
        username=EMPTY_STRING,
        password=VALID_USER["PASSWORD"],
        message_expect=MISSING_USERNAME_ERROR
    ),
    AccountData(
        username=VALID_USER["EMAIL"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR
    ),
    AccountData(
        username=VALID_USER["USERNAME"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR
    ),
    AccountData(
        username=NONEXISTENT_USER["EMAIL"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR
    ),
    AccountData(
        username=NONEXISTENT_USER["USERNAME"],
        password=EMPTY_STRING,
        message_expect=MISSING_PASSWORD_ERROR
    ),
    AccountData(
        username=EMPTY_STRING,
        password=EMPTY_STRING,
        message_expect=MISSING_USERNAME_ERROR
    )
]

MY_ACCOUNT_LOGIN_INVALID_CREDENTIALS = [
    AccountData(
        username=NONEXISTENT_USER["EMAIL"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=UNKNOWN_EMAIL_ERROR
    ),
    AccountData(
        username=NONEXISTENT_USER["USERNAME"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_USERNAME_ERROR.format(NONEXISTENT_USER["PASSWORD"])
    ),
    AccountData(
        username=VALID_USER["EMAIL"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_EMAIL_PASSWORD_ERROR.format(VALID_USER["EMAIL"])
    ),
    AccountData(
        username=VALID_USER["USERNAME"],
        password=NONEXISTENT_USER["PASSWORD"],
        message_expect=INVALID_USERNAME_PASSWORD_ERROR.format(VALID_USER["USERNAME"])
    )
]

MY_ACCOUNT_LOGIN_VALID_CREDENTIALS = [
    AccountData(
        username=VALID_USER["EMAIL"],
        password=VALID_USER["PASSWORD"]
    ),
    AccountData(
        username=VALID_USER["USERNAME"],
        password=VALID_USER["PASSWORD"]
    ),
    AccountData(
        username=VALID_ADMIN["USERNAME"],
        password=VALID_ADMIN["PASSWORD"]
    ),
    AccountData(
        username=VALID_ADMIN["USERNAME"],
        password=VALID_ADMIN["PASSWORD"]
    )
]

MY_ACCOUNT_ACCESS_WP_ADMIN_DASHBOARD = [
    AccountData(
        admin_redirect_url=WP_ADMIN_LOGIN
    ),
    AccountData(
        username=VALID_USER["USERNAME"],
        password=VALID_USER["PASSWORD"]
    ),
    AccountData(
        username=VALID_ADMIN["USERNAME"],
        password=VALID_ADMIN["PASSWORD"],
        admin_redirect_url=WP_ADMIN_DASHBOARD
    )
]

MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH = [
    AccountData(
        password=MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_VERY_WEAK["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_VERY_WEAK
    ),
    AccountData(
        password=MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_WEAK["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_WEAK
    ),
    AccountData(
        password=MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_MEDIUM["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_MEDIUM
    ),
    AccountData(
        password=MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH_STRONG["PASSWORD"],
        password_strength=PASSWORD_STRENGTH_STRONG
    )
]
