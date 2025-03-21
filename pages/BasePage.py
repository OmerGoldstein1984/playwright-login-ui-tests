from playwright.sync_api import Page

class base_page():
    def __init__(self,page:Page):
        self.page=page

    def click(self,locator):
        self.page.click(locator)

    def fill(self,locator,text):
        self.page.fill(locator,text)

    def is_visible(self,locator):
        return self.page.is_visible(self,locator)

    def wait_for_element(self,locator):
        self.page.wait_for_selector(locator,10)
