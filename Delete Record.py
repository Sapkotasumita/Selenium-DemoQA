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
driver.maximize_window()
driver.get("https://demoqa.com/webtables")
wait = WebDriverWait(driver, 10)

# -----------------------------
#  Click Add
# -----------------------------
wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()

# -----------------------------
#  Fill form and submit
# -----------------------------
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("QA")
driver.find_element(By.ID, "lastName").send_keys("Tester")
driver.find_element(By.ID, "userEmail").send_keys("qa@test.com")
driver.find_element(By.ID, "age").send_keys("25")
driver.find_element(By.ID, "salary").send_keys("60000")
driver.find_element(By.ID, "department").send_keys("Testing")

# Scroll and click submit using JS
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", submit_btn)

# Screenshot after adding
driver.save_screenshot("screenshots/webtable_added.png")
print(" Record added successfully")

time.sleep(2)

# -----------------------------
# Verify record exists
# -----------------------------
rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
found = False
for row in rows:
    if "qa@test.com" in row.text:
        found = True
        print(" Record verified in table")
        break
assert found, "Record not found in table"

# -----------------------------
# Delete record
# -----------------------------
delete_btn = driver.find_element(By.XPATH, "//span[@title='Delete']")
driver.execute_script("arguments[0].click();", delete_btn)

# Screenshot after delete
driver.save_screenshot("screenshots/webtable_deleted.png")
print(" Record deleted successfully")

# -----------------------------
driver.quit()
