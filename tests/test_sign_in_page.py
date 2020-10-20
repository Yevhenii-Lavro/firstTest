from pages.sign_in_page import SignInPage

class TestLoginPage():

    def test_shoud_be_sign_in_page(self, browser):
        self.link = "https://test.banksend.com/admin/sign-in"
        page = SignInPage(browser, self.link)
        page.open()
        page.should_be_sign_in_page()

    def test_login(self, browser):
        self.link = "https://test.banksend.com/admin/sign-in"
        page = SignInPage(browser, self.link)
        page.open()
        page.enter_username()
        page.enter_password()
        page.click_sign_in_button()
        page.user_logged()

    def test_wrong_credential(self, browser):
        self.link = "https://test.banksend.com/admin/sign-in"
        page = SignInPage(browser, self.link)
        page.open()
        page.enter_wrong_username()
        page.enter_wrong_password()
        page.click_sign_in_button()
        page.should_be_error_text()
        page.error_text_according_to_requirements()

    def test_login_as_merchant(self, browser):
        page = SignInPage(browser, self)
        page.login_as_merchant()

    def test_login_as_superadmin(self, browser):
        page = SignInPage(browser, self)
        page.login_as_superadmin()




