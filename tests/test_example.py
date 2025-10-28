import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

"""TRACING

To record a trcae

pytest --tracing on

This will create a trace.zip for each test function in test-results folder 
To view a trace.zip file

playwright show-trace <trace.zip file path>

Viewing remote traces is also possible:
playwright show-trace https://example.com/trace.zip"""

'''VIDEO CAPTURE

Videos are saved upon browser context closure at the end of a test. If you create a browser context manually, make sure to await browser_context.close().

'''