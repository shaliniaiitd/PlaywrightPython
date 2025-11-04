from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1: Define desired capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"  # ensure this matches `adb devices` output
options.automation_name = "UiAutomator2"
options.app = "/home/shalini-agarwal/Downloads/ApiDemos-debug.apk"

# Step 2: Connect to the Appium server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Step 3: Wait for app to load
time.sleep(3)

# Step 4: Locate and click the "Graphics" element
graphics_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Graphics")')
graphics_element.click()
print("✅ Clicked on 'Graphics' successfully!")

# Step 5: Pause to observe result
time.sleep(3)

# Step 6: End session
driver.quit()
