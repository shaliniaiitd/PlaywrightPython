
#find all the links on google.com

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com")
    links = page.query_selector_all("a")
    for link in links:
        print(link.get_attribute("href"))
    browser.close()
