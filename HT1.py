""" Home Task 01:
1. Install Nodejs.
2. Setup new folder named Playwright_Training .
3. Install Playwright from command line.
4. With Playwright Test Generator record a Test with below steps.
5. Navigate to https://www.google.com.
6. Enter text Playwright and hit enter key.
7. Click on the Playwright official website.
8. And Observe test script generated.
"""
from playwright.sync_api import Playwright, sync_playwright, expect

import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()

    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.get_by_role("link", name="Playwright: Fast ").click()
    time.sleep(3)
    # ---------------------
    context.close()
    browser.close()



# import time
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.com/?zx=1761424586821&no_sw_cr=1")
#     page.get_by_role("combobox", name="Search").click()
#     page.get_by_role("combobox", name="Search").fill("Playwright")
#     page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3DPlaywright%26sca_esv%3D408005786895665f%26source%3Dhp%26ei%3DyTT9aIKLJ4i6seMP-YOh2Aw%26iflsig%3DAOw8s4IAAAAAaP1C2TS3jIANfISDfHDhU63nfuEzDVmE%26ved%3D0ahUKEwjCk-f1mcCQAxUIXWwGHflBCMsQ4dUDCBA%26uact%3D5%26oq%3DPlaywright%26gs_lp%3DEgdnd3Mtd2l6IgpQbGF5d3JpZ2h0MggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyCBAAGIAEGLEDMgUQABiABDIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixA0jqLlDuCljuIXABeACQAQCYAZUBoAHGC6oBBDAuMTC4AQPIAQD4AQGYAgugAoYMqAIKwgIKEC4YAxiPARjqAsICChAAGAMYjwEY6gLCAgsQLhiDARixAxiABMICCxAAGIAEGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQLhiABBixAxiDAcICDhAAGIAEGIoFGLEDGIMBmAMOkgcEMS4xMKAHrzWyBwQwLjEwuAf4C8IHBzAuMy43LjHIByw%26sclient%3Dgws-wiz%26sei%3D1DT9aIndE865seMP_ousgQ0&q=EhAkBQIBwB76BL6rE4k3JXK5GNTp9McGIjCClu2AdN2vlAlYVSaSXWEZSfHoycPcVLnOUJIvwW0FuM0R00cp1xK4oXt2wAA-VKUyAVJaAUM")
#     # page.locator("iframe[name=\"a-ovrszjs0mggx\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
#     # page.locator("iframe[name=\"c-ovrszjs0mggx\"]").content_frame.get_by_role("button", name="Skip").click()
#     # page.locator("iframe[name=\"c-ovrszjs0mggx\"]").content_frame.locator(".rc-canonical-bridge").click()
#     # page.locator("div:nth-child(2) > div").first.click()
#     # page.locator("iframe[name=\"a-ovrszjs0mggx\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
#     # page.locator("iframe[name=\"c-ovrszjs0mggx\"]").content_frame.get_by_role("button", name="Verify").click()
#     page.get_by_role("link", name="Playwright: Fast and reliable").click()
#     time.sleep(3)
#
#     # ---------------------
#     context.close()
#     browser.close()
#
with sync_playwright() as playwright:
    run(playwright)