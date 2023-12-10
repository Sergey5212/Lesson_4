from .base_page import BasePage
from .locators import ViewBasketPage


class BasketPage(BasePage):
    def no_product_in_basket(self):
        self.products_basket_is_empty()
        self.no_products_in_basket_present()

    def products_basket_is_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*ViewBasketPage.BASKET_ZERO).text, "Basket is not empty"

    def no_products_in_basket_present(self):
        assert self.is_not_element_present(*ViewBasketPage.BASKET_TITLE), "Product in basket"

