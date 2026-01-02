import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/links")
wait = WebDriverWait(driver, 10)


# Click "Home" link (opens new tab)
home_link = wait.until(EC.element_to_be_clickable((By.ID, "simpleLink")))
home_link.click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
assert "demoqa.com" in driver.current_url
print("Home link opened correctly")
driver.save_screenshot("screenshots/link_home.png")

driver.close()
driver.switch_to.window(driver.window_handles[0])

# Test other links (skip javascript:void(0))
links_ids = ["created", "no-content", "moved", "bad-request", "unauthorized", "forbidden", "invalid-url"]

for link_id in links_ids:
    link = driver.find_element(By.ID, link_id)
    url = link.get_attribute("href")
    
    # Skip javascript links
    if url.startswith("javascript"):
        print(f"Skipping {link_id}, href is JavaScript")
        continue

    # Send GET request to real URLs
    try:
        response = requests.get(url)
        print(f"{link_id} → Status Code: {response.status_code}")
    except Exception as e:
        print(f" {link_id} → Error: {e}")

driver.save_screenshot("screenshots/link_api_status.png")
driver.quit()
