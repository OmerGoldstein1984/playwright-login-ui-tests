from time import sleep

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="C:\\Users\\omergo\\Downloads\\chromium\\chrome-win\\chrome.exe",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)
        page=context.new_page()
        page.goto('https://rahulshettyacademy.com/AutomationPractice/')
        # page.get_by_label('username:').fill('rahulshettyacademy')
        # page.get_by_label('password:').fill('learning')
        # page.get_by_role('combobox').select_option('teach')
        # page.get_by_role('link', name="terms and conditions").click()
        # page.get_by_role('button', name='Sign In').click()
        sleep(3)
        yield page
        browser.close()
