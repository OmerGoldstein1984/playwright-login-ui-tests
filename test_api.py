from playwright.sync_api import sync_playwright
from utils.ApiUtils import ApiUtils

def test_Cars():
    with sync_playwright() as playwright:
            api_utils = ApiUtils()
           # api_utils.CreteCar(playwright)
            api_utils.getCar(playwright,2)
