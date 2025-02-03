from playwright.async_api import async_playwright
from playwright.sync_api import Playwright


class ApiUtils:
    baseUrl="127.0.0.1:5000"
    def CreateOrder(self,playwright:Playwright):
        apiRequestContext= playwright.request.new_context(base_url=self.baseUrl)
        apiRequestContext.post()
        apiRequestContext.get()






