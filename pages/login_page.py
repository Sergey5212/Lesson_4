from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = self.browser.current_url
        assert "login" in link, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password form is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button form is not present"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 form is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button form is not present"
