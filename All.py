from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup

if not os.path.exists("screenshots1"):
    os.makedirs("screenshots1")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")
wait = WebDriverWait(driver, 10)

# Helper Functions

def take_screenshot(name):
    path = f"screenshots1/{name}.png"
    driver.save_screenshot(path)
    print(f" Screenshot saved: {path}")

def find_record(email):
    rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']/div")
    for row in rows:
        if email in row.text:
            return row
    return None

#  ADD Record

wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()

wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("QA")
driver.find_element(By.ID, "lastName").send_keys("Tester")
driver.find_element(By.ID, "userEmail").send_keys("qa@test.com")
driver.find_element(By.ID, "age").send_keys("28")
driver.find_element(By.ID, "salary").send_keys("70000")
driver.find_element(By.ID, "department").send_keys("Testing")

submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", submit_btn)

take_screenshot("webtable_added")
print(" Record added successfully")
time.sleep(1)


#  VERIFY Record

record = find_record("qa@test.com")
assert record is not None, " Record not found!"
print(" Record verified in table")
take_screenshot("webtable_verified")


# EDIT Record
edit_btn = record.find_element(By.XPATH, ".//span[@title='Edit']")
driver.execute_script("arguments[0].click();", edit_btn)

# Update age and department
age_field = driver.find_element(By.ID, "age")
age_field.clear()
age_field.send_keys("30")
driver.find_element(By.ID, "department").clear()
driver.find_element(By.ID, "department").send_keys("QA Automation")

driver.find_element(By.ID, "submit").click()
time.sleep(1)
take_screenshot("webtable_edited")
print(" Record edited successfully")

#  SEARCH Record

search_box = driver.find_element(By.ID, "searchBox")
search_box.clear()
search_box.send_keys("qa@test.com")
time.sleep(1)
searched_record = find_record("qa@test.com")
assert searched_record is not None, " Record not found in search!"
take_screenshot("webtable_search")
print(" Record search verified")


#  DELETE Record

delete_btn = searched_record.find_element(By.XPATH, ".//span[@title='Delete']")
driver.execute_script("arguments[0].click();", delete_btn)
time.sleep(1)

# Verify deletion
deleted_record = find_record("qa@test.com")
assert deleted_record is None, " Record still exists after deletion!"
take_screenshot("webtable_deleted")
print(" Record deleted successfully")

# -----------------------------
driver.quit()
