from playwright.sync_api import sync_playwright
from utils.ApiUtils import ApiUtils

def test_createCar():
    with sync_playwright() as playwright:
            api_utils = ApiUtils()
            api_utils.CreteCar(playwright)