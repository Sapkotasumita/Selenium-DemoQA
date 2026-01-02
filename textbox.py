from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(2)

# Fill form
driver.find_element(By.ID, "userName").send_keys("test user")
driver.find_element(By.ID, "userEmail").send_keys("user@test.com")
driver.find_element(By.ID, "currentAddress").send_keys("dhaka")
driver.find_element(By.ID, "permanentAddress").send_keys("china")

# Submit
driver.find_element(By.ID, "submit").send_keys(Keys.ENTER)
time.sleep(2)

# Verify output
output = driver.find_element(By.ID, "output").is_displayed()
assert output
print("Form submitted successfully")

#  Take Screenshot after submit
screenshot_path = "screenshots/textbox_form_success.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved at: {screenshot_path}")

driver.quit()
