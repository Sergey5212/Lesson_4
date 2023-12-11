import pytest
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestChecksOfTenSites():
    def test_guest_can_add_product_to_basket(browser, link):
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_be_page_object()


@pytest.mark.negative_checks
class TestCantSeeSuccessMessage():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.press_button()
        pages.press_code()
        pages.presence_of_element_located()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button()
        page.presence_of_element_located()


@pytest.mark.go_to_login_from_the_main_page
class TestGoToPage():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.go_to_login_page()

@pytest.mark.add_product
class TestUserAddingProduct():
    @pytest.mark.xfail
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.press_button()
        pages.press_code()
        pages.should_not_be_success_message()

@pytest.mark.inheritance_and_negative_checks
class TestBasketPage():
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        pages = ProductPage(browser, link)
        pages.open()
        pages.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.no_product_in_basket()


