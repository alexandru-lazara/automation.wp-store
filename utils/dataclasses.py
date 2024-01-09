"""Tests Dataclasses File."""

from dataclasses import dataclass

from templates.templates import EMPTY_STRING, MY_ACCOUNT_URL


@dataclass
class AccountData:
    username: str = EMPTY_STRING
    password: str = EMPTY_STRING
    password_strength: str = EMPTY_STRING
    message_expect: str = EMPTY_STRING
    admin_redirect_url: str = MY_ACCOUNT_URL
