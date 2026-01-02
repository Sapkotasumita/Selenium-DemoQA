from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Create screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click Add
wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()

# Fill form
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("QA")
driver.find_element(By.ID, "lastName").send_keys("Tester")
driver.find_element(By.ID, "userEmail").send_keys("qa@test.com")
driver.find_element(By.ID, "age").send_keys("23")
driver.find_element(By.ID, "salary").send_keys("50000")
driver.find_element(By.ID, "department").send_keys("Testing")

# Scroll to Submit button
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)

# JavaScript click (avoids intercepted click)
driver.execute_script("arguments[0].click();", submit_btn)

print(" Record added successfully")

# Screenshot
driver.save_screenshot("screenshots/webtable_record_added.png")

driver.quit()
