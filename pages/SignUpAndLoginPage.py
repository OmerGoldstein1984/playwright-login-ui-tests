from pages.BasePage import base_page


class signup_and_login(base_page):

    EMAIL= 'name="name"'
    PASSWORD = 'email="email"'
    SIGN_UP_BTN ='//input[text()="Signup"]'

    def login(self,user,password):
        self.fill(self.EMAIL,user)
        self.fill(self.PASSWORD,password)
        self.click(self.SIGN_UP_BTN)