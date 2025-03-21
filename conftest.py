from time import sleep
from playwright.sync_api import  sync_playwright

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page=context.new_page().goto("https://automationexercise.com/")
        yield page
        browser.close()
