from conftest import config
from pages.HomePage import home_page


class test_login:
    def test_registerUser_automationexcersixe(browser):
        homePage=home_page(browser,config)
        homePage.verify_Page_loaded()
        signinPage = homePage.click_sign_in()
        signinPage.verify_Page_loaded()
        signinPage.sign_up(config['username'],config['password'])
        newAccountInfoPage = signinPage.click_continue()
