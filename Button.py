from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# -----------------------------
# Setup
# -----------------------------
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# -----------------------------
#  Double Click Button
# -----------------------------
double_click_btn = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
actions.double_click(double_click_btn).perform()
time.sleep(1)

# Verify message
double_msg = driver.find_element(By.ID, "doubleClickMessage").text
assert double_msg == "You have done a double click"
print("Double click verified")

driver.save_screenshot("screenshots/button_double_click.png")

# -----------------------------
# Right Click Button
# -----------------------------
right_click_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_click_btn).perform()
time.sleep(1)

right_msg = driver.find_element(By.ID, "rightClickMessage").text
assert right_msg == "You have done a right click"
print(" Right click verified")

driver.save_screenshot("screenshots/button_right_click.png")

# -----------------------------
#  Dynamic Click Button (Click Me)
# -----------------------------
click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
click_me_btn.click()
time.sleep(1)

dynamic_msg = driver.find_element(By.ID, "dynamicClickMessage").text
assert dynamic_msg == "You have done a dynamic click"
print("Dynamic click verified")

driver.save_screenshot("screenshots/button_click_me.png")

# -----------------------------
driver.quit()
