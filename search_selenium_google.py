from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page = browser.new_page()
    page.goto("https://www.google.com")
    time.sleep(2)
    element = page.locator("#APjFqb")
    element.fill("Playwright")
    #page.fill("#APjFqb", "Playwright")

    element.press("Enter")  # ✅ Press Enter key
    page.wait_for_load_state("networkidle")
    time.sleep(5)
    print(page.title())

    browser.close()