# Configuration file for Playwright in Python

config = {
    "base_url": "https://datatables.net/examples/data_sources/server_side",
    "browser": "chromium",  # Options: "chromium", "firefox", "webkit"
    "headless": False,      # Set to True to run in headless mode
    "timeout": 30000,       # Timeout for actions (in ms)
    "retries": 2            # Number of retries for failed tests
}
