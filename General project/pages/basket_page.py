from .locators import ViewBasketPage
from .base_page import BasePage


class BasketPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.browser.find_element(*ViewBasketPage.VIEW_BASKET).click()
        assert self.is_disappeared(*ViewBasketPage.BASKET_ZERO), "The product is in the basket"
