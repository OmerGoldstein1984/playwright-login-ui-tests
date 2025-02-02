from playwright.async_api import Playwright,async_playwright
class ApiUtils:
    baseUrl="127.0.0.1:5000"
    def CreateOrder(self,playwright:Playwright):
        apiRequestontext=playwright.request.new_context(base_url=self.baseUrl).post()
        apiRequestontext.po

