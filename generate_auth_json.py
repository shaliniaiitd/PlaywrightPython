from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to Google and manually log in / solve captcha once
    page.goto("https://accounts.google.com/signin")

    input("Press Enter after logging in and captcha is solved...")

    # Save storage (cookies, localStorage, etc.)
    context.storage_state(path="auth.json")
    browser.close()
