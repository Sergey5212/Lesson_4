from pages.locators import ViewBasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    pages = MainPage(browser, link)
    pages.open()
    pages.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    pages = MainPage(browser, link)
    pages.open()
    pages.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    pages = MainPage(browser, link)
    pages.open()
    browser.find_element(*ViewBasketPage.VIEW_BASKET).click()
    assert "Your basket is empty" in browser.find_element(*ViewBasketPage.BASKET_ZERO).text, "The product is in the basket"
