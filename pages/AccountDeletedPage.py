class AccountDeletedPage:
    ACCOUNT_DELETED_TEXT = "//b[text()='Account Deleted!']"
    CONTINUE_BTN = "//a[text()='Continue']"
    def verify_Page_loaded(self):
        self.wait_for_element(self.ACCOUNT_DELETED_TEXT)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)