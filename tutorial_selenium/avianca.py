from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.maximize_window()

driver.get("https://www.avianca.com/co/es/")

time.sleep(2)
driver.quit()