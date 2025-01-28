from time import sleep

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="C:\\Users\\omergo\\Downloads\\chromium\\chrome-win\\chrome.exe",
            headless=False
        )
        yield browser
        browser.close()
