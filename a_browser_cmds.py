

'''Convert following to plawright from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

url = "https://www.google.co.in/"

print ("title", driver.title)

driver.get(url)
#current url
print("Current Url", driver.current_url)
'''
from collections import namedtuple

# ENV PREPARATION
'''
Good catch, Shalini — that error means the **virtual environment folder name** you created (`play_ venv`) has a **space** in it.
So Python actually created a folder named `play_` and maybe ignored `venv`, or vice versa — hence there’s no `play_venv/bin/activate` path.

Let’s fix this cleanly 👇

---



### ✅ **Step-by-Step Fix**

1. **Remove the incorrectly created folder (optional):**

```bash
rm -rf play_ venv
```

2. **Create a new virtual environment (no spaces in name):**

```bash
python3 -m venv play_venv
```

3. **Activate it:**

```bash
source play_venv/bin/activate
```

4. **You’ll see your prompt change**, something like:

```
(play_venv) shalini-agarwal@your-machine:~/PlaywrightPython$
```

5. **Now install Playwright:**

```bash
pip install playwright pytest-playwright
```

6. **Install browsers:**

```bash
playwright install
```

7. **Verify it works:**

```bash
python -m playwright codegen https://example.com

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False)
        #browser = browser_type.launch(headless=False, channel = 'msedge')
        print("Browser name:", browser_type.name)

        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.co.in/", wait_until="domcontentloaded")
        print(page.title())


        page.goto("https://www.yahoo.com", wait_until="domcontentloaded")
        print(page.title())

        #Navigate back and forward

        '''
        Advantages of expect_navigation():
    
    Handles SPAs or heavy JS pages
    
    Ensures your next line runs after navigation completes
    
    🔹 Interview Tip
    
    “Unlike Selenium, Playwright’s go_back() / go_forward() are fire-and-forget. You should always combine them with 
    page.wait_for_load_state() or page.expect_navigation() to ensure the page has finished loading before interacting.”
        
        '''
        # # Go back with explicit wait
        # with page.expect_navigation(wait_until="domcontentloaded"):
        #     page.go_back()
        # print("Back to:", page.title())
        #
        # # Go forward with explicit wait
        # with page.expect_navigation(wait_until="domcontentloaded"):
        #     page.go_forward()
        # print("Forward to:", page.title())

        # Go back
        # page.go_back()
        # page.wait_for_load_state("domcontentloaded")  # waits until DOM is ready
        # print("Back to:", page.title())
        #
        # # Go forward
        # page.go_forward()
        # page.wait_for_load_state("domcontentloaded")
        # print("Forward to:", page.title())

        #3rd way
        page.go_back(wait_until="domcontentloaded", timeout=60000)
        print(page.title())

        page.go_forward(wait_until="domcontentloaded", timeout=60000)
        print(page.title())    #Close the browser


        import time
        # Minimize (simulate by setting to very small size)
        page.set_viewport_size({"width": 100, "height": 100})
        print("Minimized viewport")

        page.reload(wait_until="domcontentloaded", timeout=60000)

        time.sleep(3)

        # Maximize (simulate by setting to a large resolution)
        page.set_viewport_size({"width": 1920, "height": 1080})
        print("Maximized viewport")

        time.sleep(3)  # inorder to view

        #get browser name







        '''
        elenium
        
        driver.close() → Closes the current window/tab.
        
        driver.quit() → Closes all windows and ends the WebDriver session.
        
        Playwright
        
        page → Represents a single tab/page.
        
        context → Represents a browser session (isolated cookies, storage, etc.).
        
        browser → Represents the browser process itself.
        
        Closing methods:
        
        Object	Close method	Effect
        page	page.close()	Closes that tab
        context	context.close()	Closes all pages in that context
        browser	browser.close()	Closes the entire browser process
        '''

        #COOKIE MANAGEMENT

        # Access cookies
        cookies = context.cookies()
        print("All cookies:", cookies)

        # Delete all cookies
        context.clear_cookies()
        print("Deleted all cookies. Now:", context.cookies())

        # Add a new cookie
        context.add_cookies([{"name": "shalini","value": "agarwal","domain": ".google.com","path": "/"
        }])

        print("After adding a cookie:", context.cookies())

        '''
        #Accessing page source

print ("page source", driver.page_source)
print ("page source length", len(driver.page_source))
'''
        page_source = page.content()
        print("Page source:", page_source)
        print("Page source length:", len(page_source))

        # WINDOWS
        """
        #Multiple windows

        print ("current window", driver.current_window_handle) """

        window_handle = context.pages.index(page)
        print(f"Current window: {window_handle}")

        """print("No. of open windows", len(driver.window_handles))
        """

        print(f"Number of open  windows:  {len(context.pages)}")




    browser.close()