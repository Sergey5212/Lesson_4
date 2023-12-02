import pytest
from pages.product_page import ProductPage


@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.press_button()
    pages.press_code()
    pages.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.press_button()
    pages.press_code()
    pages.presence_of_element_located()
