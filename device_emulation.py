'''Generate this code using following at command line:
playwright codegen --device="Pixel 5" playwright.dev '''

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(**playwright.devices["Pixel 5"])
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("button", name="On this page").click()
    page.get_by_role("link", name="HTML Test Reports", exact=True).click()
    page.goto("https://playwright.dev/docs/intro")
   #  page.get_by_role("link", name="What's next", exact=True).click()
    page.get_by_text("Learn", exact=True).click()
    page.get_by_role("link", name="Getting started").click()

    # ---------------------
    context.close()

    context = browser.new_context(**playwright.devices["Desktop Edge HiDPI"])
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="API").click()
    page.get_by_role("button", name="Search (Ctrl+K)").click()
    page.get_by_role("searchbox", name="Search").fill("how to write an api test")
    page.get_by_role("searchbox", name="Search").press("Enter")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
