from time import sleep
from playwright.sync_api import  sync_playwright

import pytest
from playwright.sync_api import sync_playwright

from utils.ConfigLoader import ConfigLoader


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against")

@pytest.fixture(scope="session")
def config(request):
    return ConfigLoader(request.config.getoption("--env")).load_config()
@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        url = config['base_url']
        page=context.new_page().goto(url)
        yield page
        browser.close()
        context.close()