
import pytest
from playwright.sync_api import Playwright, sync_playwright, Page



@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")


@pytest.fixture(scope="function", autouse=True)
def start_tracing(context):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    context.tracing.stop(path="trace.zip")

@pytest.fixture(scope="function")
def context(browser):
    return browser.new_context(record_video_dir="videos/")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"storage_state": "auth.json"}

