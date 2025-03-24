
class AccountCreatedSecussesfuly_page:
    ACCOUNT_CREATED_SUCCESSFULLY_TEXT = "//b[text()='Account Created!']"
    CONTINUE_BTN = "//a[text()='Continue']"
    def verify_Page_loaded(self):
        self.wait_for_element(self.ACCOUNT_CREATED_SUCCESSFULLY_TEXT)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)