import pytest
from playwright.sync_api import sync_playwright
from utils.ConfigLoader import ConfigLoader
import os

@pytest.fixture(scope="session")
def browser_type_launch_args():
    is_headless = os.environ.get("CI", "false").lower() == "true"
    return {"headless": is_headless}

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against")

@pytest.fixture(scope="session")
def config(request):
    return ConfigLoader(request.config.getoption("--env")).load_config()
@pytest.fixture(scope="session")
def browser(config,browser_type_launch_args):
    with sync_playwright(browser_type_launch_args) as p:
        browser = p.chromium.launch(args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        url = config['base_url']
        print(f"current url: {url}\n")
        print(f"environment: {config['env']}\n")
        page=context.new_page().goto(url)
        yield page
        browser.close()
        context.close()