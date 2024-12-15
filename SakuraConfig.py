from playwright.sync_api import sync_playwright
import time
from playwright_config import config


with sync_playwright() as p:
    # Initialize browser with config file
    browser_type = getattr(p, config["browser"])
    browser = browser_type.launch(headless=config["headless"])
    context = browser.new_context()
    page = context.new_page()

    # Set base URL from config
    page.goto(config["base_url"])

    # Perform actions with the specified timeout
    page.set_default_timeout(config["timeout"])

    while True:
        try:
            # Wait for table rows to be loaded
            rows = page.locator('//table[@id="example"]/tbody/tr')
            rows_count = rows.count()

            # Loop through each row to find "Sakura"
            for i in range(rows_count):
                first_td = rows.nth(i).locator('td:nth-child(1)')  # Use CSS selector for child locator
                if first_td.inner_text() == "Sakura":
                    # Print all <td> text within this row
                    all_tds = rows.nth(i).locator('td')  # Use CSS selector for all <td> in the row
                    all_tds_count = all_tds.count()
                    for j in range(all_tds_count):
                        print(all_tds.nth(j).inner_text())
                    browser.close()
                    exit()  # Exit the script after finding the match

            # Check if the "Next" button is enabled (class does not have 'disabled')
            next_button = page.locator('//button[@class="dt-paging-button next" and not(contains(@class, "disabled"))]')
            time.sleep(5)
            if next_button.count() == 0:  # If no enabled "Next" button exists, break the loop
                print("Reached the last page or 'Next' button is disabled.")
                break

            # Click the "Next" button
            next_button.click()
            page.wait_for_load_state("domcontentloaded")  # Wait for the next page to load

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    browser.close()
