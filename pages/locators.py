from selenium.webdriver.common.by import By


class AddingToLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, '.alertinner > strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    PRICE_PRODUCT_IN_CART = (By.CSS_SELECTOR, '.alertinner p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class ViewBasketPage():
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn-default")
    BASKET_ZERO = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")

