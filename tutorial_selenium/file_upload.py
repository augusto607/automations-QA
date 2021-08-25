# Import selenium webdriver
from selenium import webdriver

import time

# Instantiate webdriver for firefox
driver = webdriver.Firefox(executable_path="drivers/geckodriver")
# Open URL
driver.get("http://testautomationpractice.blogspot.com/")
# Maximize window
driver.maximize_window()

# We focus in frame that contain our element
driver.switch_to.frame("frame-one1434677811")
# Find the desired element
file_upload_btn = driver.find_element_by_id("RESULT_FileUpload-10")
# We need to give the file path to upload
file_upload_btn.send_keys("/Users/augusto607/Documents/Images/avatars/no-avatar.jpg")

time.sleep(2)
# Kill Instance
driver.quit()