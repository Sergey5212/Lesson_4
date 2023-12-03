from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ViewBasketPage
from .base_page import BasePage
from .product_page import ProductPage


class BasketPage():
    def no_product_in_basket(self):
        self.press_button()
        self.product_name_matches_the_one_added()
        self.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    def product_in_basket_present(self):
        assert self.is_not_present_product_in_basket(*ViewBasketPage.BASKET_ZERO), "Product in basket"

