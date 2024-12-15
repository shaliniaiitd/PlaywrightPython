from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor

# Define the test logic for a single browser
def run_test(browser_name):
    try:
        with sync_playwright() as p:
            # Dynamically get the browser type
            browser_type = getattr(p, browser_name)
            browser = browser_type.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Navigate to the test URL
            page.goto("https://datatables.net/examples/data_sources/server_side")

            # Locate rows in the table and print some information
            rows = page.locator('//table[@id="example"]/tbody/tr')
            print(f"{browser_name}: Found {rows.count()} rows on the page.")

            # Close the browser
            browser.close()

    except Exception as e:
        print(f"Test failed on {browser_name}: {e}")

# List of browsers to test
browsers = ["chromium", "firefox", "webkit"]

# Run the test concurrently on all browsers
with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
    executor.map(run_test, browsers)
