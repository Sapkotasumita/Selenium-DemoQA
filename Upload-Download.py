from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil

# Setup

download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
upload_file_path = os.path.join(download_dir, "samplefile.jpeg")  

if not os.path.exists("screenshots_upload"):
    os.makedirs("screenshots_upload")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/upload-download")
wait = WebDriverWait(driver, 10)

#  File Upload

upload_input = wait.until(EC.presence_of_element_located((By.ID, "uploadFile")))
upload_input.send_keys(upload_file_path)  # Sends the local file path to upload input
time.sleep(1)

# Verify uploaded file
uploaded_file_name = driver.find_element(By.ID, "uploadedFilePath").text
assert "samplefile.jpeg" in uploaded_file_name
print(" File uploaded successfully:", uploaded_file_name)
driver.save_screenshot("screenshots_upload/upload_file.png")


#  File Download

download_btn = driver.find_element(By.ID, "downloadButton")
download_btn.click()
time.sleep(3)  # Wait for download to complete

# Verify download (check if file exists in Downloads)
downloaded_file = os.path.join(download_dir, "sampleFile.jpeg")
if os.path.exists(downloaded_file):
    print(" File downloaded successfully:", downloaded_file)
    shutil.move(downloaded_file, os.path.join(os.getcwd(), "screenshots_upload", "downloaded_sampleFile.jpeg"))
    print(" Downloaded file moved to project folder")
else:
    print(" File download failed")

driver.save_screenshot("screenshots_upload/download_file.png")

driver.quit()
