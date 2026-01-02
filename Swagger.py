from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# Setup
if not os.path.exists("screenshots_swagger"):
    os.makedirs("screenshots_swagger")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/swagger/")
wait = WebDriverWait(driver, 15)  # increase wait for dynamic content


# Verify Swagger UI loaded

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swagger-ui")))
print(" Swagger UI loaded successfully")
driver.save_screenshot("screenshots_swagger/swagger_ui.png")

# Expand the first API endpoint

endpoint = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(@class,'opblock-summary-control')]")
))
endpoint.click()
time.sleep(1)
driver.save_screenshot("screenshots_swagger/endpoint_expanded.png")
print("First API endpoint expanded")


# Click 'Try it out'

try_it_out_btn = driver.find_element(By.XPATH, "//button[contains(@class,'try-out')]")
try_it_out_btn.click()
time.sleep(1)


# Execute API

execute_btn = driver.find_element(By.XPATH, "//button[contains(@class,'execute')]")
execute_btn.click()
time.sleep(3)  # wait for response


# Verify response

response_code = driver.find_element(By.XPATH, "//td[@class='response-col_status']").text
print(" Response status code:", response_code)
driver.save_screenshot("screenshots_swagger/response.png")

driver.quit()
