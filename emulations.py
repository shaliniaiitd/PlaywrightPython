import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    '''
    1) EMULATE VIEWPORT
    # playwright codegen --viewport-size="800,600" playwright.dev
    context = browser.new_context(viewport={"width":800,"height":600})

    2) EMULATE COLOR SCHEME
    # playwright codegen --color-scheme=dark playwright.dev
    context = browser.new_context(color_scheme="dark")
    
    3) Emulate geolocation, language and timezone
    
    playwright codegen --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" bing.com/maps
    
    context = browser.new_context(geolocation={"latitude":41.890221,"longitude":12.492348}, locale="it-IT", permissions=["geolocation"], timezone_id="Europe/Rome")
    page = context.new_page()
    page.goto("https://www.bing.com/maps?cp=17.503077%7E78.404167&lvl=4&style=r")
    
    4) Preserve authenticated state

Run codegen with --save-storage to save cookies, localStorage and IndexedDB data at the end of the session. This is useful to separately record an authentication step and reuse it later when recording more tests.

playwright codegen github.com/microsoft/playwright --save-storage=auth.json

  context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/microsoft/playwright")
    
    

    # ---------------------
    context.storage_state(path="auth.json")
    
    

    page = context.new_page()
    page.goto("https://playwright.dev/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


