from pages.BasePage import base_page

class home_page(base_page):
    LOOO = ".logo a img"
    SIGN_UP_IN = '.fa-lock'
    HOME = 'fa-home'
    DELETE_ACCOUNT = '.fa-trash-o'

    def verify_Page_loaded(self):
        self.wait_for_element(self.HOME)

    def click_sign_in(self):
        self.click(self.SIGN_UP_IN)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT)

        


