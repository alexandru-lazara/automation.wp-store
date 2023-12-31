"""Tests Selectors File."""

from templates.templates import MY_ACCOUNT_ENDPOINTS

# ### General Purpose Attributes ####################################
# ###################################################################

STYLE_DISPLAY_NONE = "[@style='display: none;']"

# ### Kenta Theme Selectors #########################################
# ###################################################################

XPATH_KENTA_PRELOADER_PRESET_1 = "div[@class='kenta-preloader-wrap kenta-preloader-preset-1']"
XPATH_KENTA_PRELOADER_PRESET_2 = "div[@class='kenta-preloader-wrap kenta-preloader-preset-2']"
XPATH_KENTA_PRELOADER_PRESET_3 = "div[@class='kenta-preloader-wrap kenta-preloader-preset-3']"

# ### Woocommerce Selectors #########################################
# ###################################################################

XPATH_WOOCOMMERCE = "div[@class='woocommerce']"

XPATH_PAGE_HEADING = "//div[@class='card-content flex-grow']/div/h6"

# ### Woocommerce Notices Wrapper Selectors #########################
# ###################################################################

XPATH_NOTICES_WRAPPER = "div[@class='woocommerce-notices-wrapper']"
XPATH_ERROR = "ul[@class='woocommerce-error']"

XPATH_NOTICES_WRAPPER_ERROR = (
    f"//{XPATH_NOTICES_WRAPPER}/{XPATH_ERROR}"
)

# ### My Account Selectors ##########################################
# ###################################################################

XPATH_CUSTOMER_LOGIN = "div[@id='customer_login']"
XPATH_LOGIN_DIV = "div[@class='u-column1 col-1']"
XPATH_REGISTER_DIV = "div[@class='u-column2 col-2']"
XPATH_USER = "form/p[1]"
XPATH_PASSW0RD = "form/p[2]"
XPATH_REMEMBER_ME = "form/p[3]"
XPATH_BUTTON = "form/p[3]/button"
XPATH_BUTTON_DISABLED = "form/p[3]/button[@disabled='disabled']"
XPATH_LOST_PASSW0RD = "form/p[4]"
XPATH_PRIVACY_POLICY = "form/div/p"

# ### My Account Login Section Selectors

XPATH_MY_ACCOUNT_LOGIN_SECTION = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}"
)
XPATH_MY_ACCOUNT_LOGIN_HEADING = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/h2"
)
XPATH_MY_ACCOUNT_LOGIN_USERNAME_LABEL = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_USER}/label"
)
XPATH_MY_ACCOUNT_LOGIN_USERNAME_INPUT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_USER}/input"
)
XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_LABEL = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_PASSW0RD}/label"
)
XPATH_MY_ACCOUNT_LOGIN_PASSW0RD_INPUT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_PASSW0RD}/span/input"
)
XPATH_MY_ACCOUNT_LOGIN_REMEMBER_ME_LABEL = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_REMEMBER_ME}/label/span"
)
XPATH_MY_ACCOUNT_LOGIN_REMEMBER_ME_INPUT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_REMEMBER_ME}/label/input"
)
XPATH_MY_ACCOUNT_LOGIN_LOG_IN_BUTTON = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_BUTTON}"
)
XPATH_MY_ACCOUNT_LOGIN_LOST_PASSWORD = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_LOGIN_DIV}/{XPATH_LOST_PASSW0RD}/a"
)

# ### My Account Register Section Selectors

XPATH_MY_ACCOUNT_REGISTER_SECTION = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}"
)
XPATH_MY_ACCOUNT_REGISTER_HEADING = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/h2"
)
XPATH_MY_ACCOUNT_REGISTER_USERNAME_LABEL = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_USER}/label"
)
XPATH_MY_ACCOUNT_REGISTER_USERNAME_INPUT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_USER}/input"
)
XPATH_MY_ACCOUNT_REGISTER_PASSW0RD_LABEL = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_PASSW0RD}/label"
)
XPATH_MY_ACCOUNT_REGISTER_PASSWORD_INPUT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_PASSW0RD}/span/input"
)
XPATH_MY_ACCOUNT_REGISTER_PASSWORD_STRENGTH = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_PASSW0RD}/span/div"
)
XPATH_MY_ACCOUNT_REGISTER_PASSWORD_HINT = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_PASSW0RD}/span/small"
)
XPATH_MY_ACCOUNT_REGISTER_BUTTON = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_BUTTON}"
)
XPATH_MY_ACCOUNT_REGISTER_BUTTON_DISABLED = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_BUTTON_DISABLED}"
)
XPATH_MY_ACCOUNT_REGISTER_PRIVACY_POLICY = (
    f"//{XPATH_WOOCOMMERCE}/{XPATH_CUSTOMER_LOGIN}/{XPATH_REGISTER_DIV}/{XPATH_PRIVACY_POLICY}"
)

# ### My Account Navigation Link Selectors

XPATH_MY_ACCOUNT_NAVIGATION = (
    "//nav[@class='woocommerce-MyAccount-navigation']"
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK = (
    "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--{endpoint}']/a"
)

XPATH_MY_ACCOUNT_NAVIGATION_LINK_DASHBOARD = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['DASHBOARD'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_ORDERS = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['ORDERS'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_VIEW_ORDER = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['VIEW_ORDER'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_DOWNLOADS = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['DOWNLOADS'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ACCOUNT = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['EDIT_ACCOUNT'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_EDIT_ADDRESS = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['EDIT_ADDRESS'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_PAYMENT_METHODS = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['PAYMENT_METHODS'] + "{status}")
)
XPATH_MY_ACCOUNT_NAVIGATION_LINK_LOGOUT = (
    XPATH_MY_ACCOUNT_NAVIGATION_LINK.format(endpoint=MY_ACCOUNT_ENDPOINTS['LOGOUT'])
)
