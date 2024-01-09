"""Tests Templates File."""

from tests.config import HOSTNAME, SCHEME

# ### General Purpose URLs ##########################################
# ###################################################################

EXAMPLE_URL = f"{SCHEME}://example.com/"

# ### General Purpose Constants #####################################
# ###################################################################

EMPTY_STRING = ""
NOT_ACTIVE = ""
IS_ACTIVE = " is-active"

# ### WordPress Admin URLs ##########################################
# ###################################################################

WP_ADMIN_DASHBOARD = f"{SCHEME}://{HOSTNAME}/wp-admin/"
WP_ADMIN_LOGIN = f"{SCHEME}://{HOSTNAME}/wp-login.php"

# ### WordPress Store URLs ##########################################
# ###################################################################

PRODUCTS_URL = f"{SCHEME}://{HOSTNAME}/"
MY_ACCOUNT_URL = f"{SCHEME}://{HOSTNAME}/my-account/"
CART_URL = f"{SCHEME}://{HOSTNAME}/cart/"
CHECKOUT_URL = f"{SCHEME}://{HOSTNAME}/checkout/"

MY_ACCOUNT_ENDPOINTS = {
    "DASHBOARD": "dashboard",
    "ORDERS": "orders",
    "VIEW_ORDER": "view-order",
    "DOWNLOADS": "downloads",
    "EDIT_ACCOUNT": "edit-account",
    "EDIT_ADDRESS": "edit-address",
    "PAYMENT_METHODS": "payment-methods",
    "LOST_PASSWORD": "lost-password",
    "LOGOUT": "customer-logout"
}

MY_ACCOUNT_ORDERS_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['ORDERS']}/"
MY_ACCOUNT_VIEW_ORDER_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['VIEW_ORDER']}/"
MY_ACCOUNT_DOWNLOADS_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['DOWNLOADS']}/"
MY_ACCOUNT_EDIT_ACCOUNT_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['EDIT_ACCOUNT']}/"
MY_ACCOUNT_EDIT_ADDRESSES_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['EDIT_ADDRESS']}/"
MY_ACCOUNT_PAYMENT_METHODS_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['PAYMENT_METHODS']}/"
MY_ACCOUNT_LOST_PASSWORD_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['LOST_PASSWORD']}/"
MY_ACCOUNT_LOGOUT_URL = f"{MY_ACCOUNT_URL}{MY_ACCOUNT_ENDPOINTS['LOGOUT']}/"

CHECKOUT_ENDPOINTS = {
    "PAY": "order-pay",
    "ORDER_RECEIVED": "order-received",
    "ADD_PAYMENT_METHOD": "add-payment-method",
    "DELETE_PAYMENT_METHOD": "delete-payment-method",
    "SET_DEFAULT_PAYMENT_METHOD": "set-default-payment-method"
}

CHECKOUT_PAY_URL = f"{CHECKOUT_URL}{CHECKOUT_ENDPOINTS['PAY']}/"
CHECKOUT_ORDER_RECEIVED_URL = f"{CHECKOUT_URL}{CHECKOUT_ENDPOINTS['ORDER_RECEIVED']}/"
CHECKOUT_ADD_PAYMENT_METHOD_URL = f"{CHECKOUT_URL}{CHECKOUT_ENDPOINTS['ADD_PAYMENT_METHOD']}/"
CHECKOUT_DELETE_PAYMENT_METHOD_URL = f"{CHECKOUT_URL}{CHECKOUT_ENDPOINTS['DELETE_PAYMENT_METHOD']}/"
CHECKOUT_SET_DEFAULT_PAYMENT_METHOD_URL = f"{CHECKOUT_URL}{CHECKOUT_ENDPOINTS['SET_DEFAULT_PAYMENT_METHOD']}/"

# ### WordPress My Account - Login Section ##########################
# ###################################################################

HEADING_LOGIN = "Login"
LABEL_LOGIN_USERNAME = "Username or email address *"
LABEL_LOGIN_PASSW0RD = "Password *"
LABEL_LOGIN_REMEMBER_ME = "Remember me"
LABEL_LOGIN_BUTTON = "Log In"
LABEL_LOGIN_LOST_PASSW0RD = "Lost your password?"

MISSING_USERNAME_ERROR = (
    "Error: Username is required."
)
MISSING_PASSWORD_ERROR = (
    "Error: The password field is empty."
)
UNKNOWN_EMAIL_ERROR = (
    "Unknown email address. "
    "Check again or try your username."
)
INVALID_USERNAME_ERROR = (
    "Error: The username {} is not registered on this site. "
    "If you are unsure of your username, try your email address instead."
)
INVALID_EMAIL_PASSWORD_ERROR = (
    "Error: The password you entered for the email address {} is incorrect. "
    "Lost your password?"
)
INVALID_USERNAME_PASSWORD_ERROR = (
    "Error: The password you entered for the username {} is incorrect. "
    "Lost your password?"
)

# ### WordPress My Account - Registration Section ###################
# ###################################################################

HEADING_REGISTER = "Register"
LABEL_REGISTER_EMAIL = "Email address *"
LABEL_REGISTER_PASSW0RD = "Password *"
LABEL_REGISTER_BUTTON = "Register"
LABEL_REGISTER_PRIVACY_POLICY = (
    "Your personal data will be used to support your experience throughout this website, "
    "to manage access to your account, and for other purposes described in our privacy policy."
)

PASSWORD_STRENGTH_VERY_WEAK = "Very weak - Please enter a stronger password."
PASSWORD_STRENGTH_WEAK = "Weak - Please enter a stronger password."
PASSWORD_STRENGTH_MEDIUM = "Medium"
PASSWORD_STRENGTH_STRONG = "Strong"
PASSWORD_HINT = (
    "Hint: The password should be at least twelve characters long. "
    "To make it stronger, use upper and lower case letters, numbers, and symbols like ! \" ? $ % ^ & )."
)

INVALID_REGISTER_EMAIL_ERROR = (
    "Error: Please provide a valid email address."
)
INVALID_REGISTER_PASSWORD_ERROR = (
    "Error: Please enter an account password."
)
INVALID_ALREADY_REGISTERED_MESSAGE = (
    "Error: An account is already registered with your email address. "
    "Please log in."
)

# ### Wordpress My Account - Navigation #############################
# ###################################################################

HEADING_MY_ACCOUNT = "My Account"
HEADING_ORDERS = "Orders"
HEADING_DOWNLOADS = "Downloads"
HEADING_ADDRESSES = "Addresses"
HEADING_ACCOUNT_DETAILS = "Account details"

LABEL_DASHBOARD = "Dashboard"
LABEL_ORDERS = "Orders"
LABEL_DOWNLOADS = "Downloads"
LABEL_ADDRESSES = "Addresses"
LABEL_ACCOUNT_DETAILS = "Account details"
LABEL_LOGOUT = "Log out"

DASHBOARD_HELLO_USER_MESSAGE = (
    "Hello {name} (not {name}? Log out)"
)
DASHBOARD_INTERACTIONS_MESSAGE = (
    "From your account dashboard you can view your recent orders, "
    "manage your shipping and billing addresses, and edit your password and account details."
)
