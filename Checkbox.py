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
driver.get("https://demoqa.com/checkbox")

wait = WebDriverWait(driver, 10)

# Expand Home node
expand_btn = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@title='Expand all']"))
)
expand_btn.click()

# Click Home checkbox (label click is more reliable)
home_checkbox_label = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//label[@for='tree-node-home']"))
)

# Scroll into view
driver.execute_script("arguments[0].scrollIntoView(true);", home_checkbox_label)
time.sleep(1)

home_checkbox_label.click()

# Verify checkbox selected
home_checkbox = driver.find_element(By.ID, "tree-node-home")
assert home_checkbox.is_selected()
print(" Home checkbox selected successfully")

# Screenshot
driver.save_screenshot("screenshots/checkbox_home_selected.png")

driver.quit()
