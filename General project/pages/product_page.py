from .base_page import BasePage
from .locators import AddingToLocators


class ProductPage(BasePage):
    def press_button(self):
        self.browser.find_element(*AddingToLocators.ADD_TO_BASKET).click()

    def press_code(self):
        self.solve_quiz_and_get_code()

    def presence_of_element_located(self):
        assert self.is_disappeared(*AddingToLocators.PRODUCT_NAME_IN_CART), "Erroneous success message. Explicit Wait"

    def product_name_matches_the_one_added(self):
        name_product = self.browser.find_element(*AddingToLocators.PRODUCT_NAME).text
        product_in_cart = self.browser.find_element(*AddingToLocators.PRODUCT_NAME_IN_CART).text
        assert name_product == product_in_cart, 'The product name does not match what was added'

    def should_be_page_object(self):
        self.press_button()
        self.press_code()
        self.product_name_matches_the_one_added()
        self.the_price_of_the_cart_is_the_same_as_the_price_of_the_product()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddingToLocators.PRODUCT_NAME_IN_CART), "Erroneous success message"

    def the_price_of_the_cart_is_the_same_as_the_price_of_the_product(self):
        price_product = self.browser.find_element(*AddingToLocators.PRICE_PRODUCT).text
        price_in_cart = self.browser.find_element(*AddingToLocators.PRICE_PRODUCT_IN_CART).text
        assert price_product == price_in_cart, 'The price of the cart does not match the price of the product'

