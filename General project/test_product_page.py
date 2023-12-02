import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage


class TestTenSites():
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(browser, link):
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_be_page_object()

class TestUserAddToBasketFromProductPage():
    def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.press_button()
        pages.press_code()
        pages.should_not_be_success_message()

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_not_be_success_message()

class TestQuestLoginProductPage():
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.go_to_login_page()

class TestViewBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = BasketPage(browser, link)
        pages.open()
        pages.test_guest_cant_see_product_in_basket_opened_from_product_page()