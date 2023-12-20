"""Tests Templates File."""

from tests.config import HOSTNAME, SCHEME

# ### WordPress Store URLs ##########################################
# ###################################################################

EXAMPLE_URL = f"{SCHEME}://example.com/"

PRODUCTS_URL = f"{SCHEME}://{HOSTNAME}/"
MY_ACCOUNT_URL = f"{SCHEME}://{HOSTNAME}/my-account/"
MY_ACCOUNT_ORDERS_URL = f"{SCHEME}://{HOSTNAME}/my-account/orders/"
MY_ACCOUNT_DOWNLOADS_URL = f"{SCHEME}://{HOSTNAME}/my-account/downloads/"
MY_ACCOUNT_ADDRESSES_URL = f"{SCHEME}://{HOSTNAME}/my-account/edit-address/"
MY_ACCOUNT_PAYMENT_METHODS_URL = f"{SCHEME}://{HOSTNAME}/my-account/payment-methods/"
MY_ACCOUNT_ACCOUNT_DETAILS_URL = f"{SCHEME}://{HOSTNAME}/my-account/edit-account/"
MY_ACCOUNT_LOGOUT_URL = f"{SCHEME}://{HOSTNAME}/my-account/customer-logout/"
CART_URL = f"{SCHEME}://{HOSTNAME}/cart/"
CHECKOUT_URL = f"{SCHEME}://{HOSTNAME}/checkout/"
