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
driver.get("https://demoqa.com/radio-button")

wait = WebDriverWait(driver, 10)

# Click Yes radio button (label click is reliable)
yes_radio_label = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//label[@for='yesRadio']"))
)

# Scroll into view
driver.execute_script("arguments[0].scrollIntoView(true);", yes_radio_label)
time.sleep(1)

yes_radio_label.click()

# Verify Yes radio is selected
yes_radio = driver.find_element(By.ID, "yesRadio")
assert yes_radio.is_selected()
print(" Yes radio button selected successfully")

# Verify success message
result_text = driver.find_element(By.CLASS_NAME, "text-success").text
assert result_text == "Yes"
print("Result message verified")

# Screenshot
driver.save_screenshot("screenshots/radio_yes_selected.png")

driver.quit()
