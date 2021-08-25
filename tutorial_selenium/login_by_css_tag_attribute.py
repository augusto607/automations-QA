# Importamos webdriver desde selenium
from selenium import webdriver
import time

# Instanciamos una variable con la ruta del ejecutable del navegador
driver = webdriver.Chrome(executable_path="drivers/chromedriver")

# Obtenemos la url de nuestra app con el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Buscamos los elemento por la etiqueta css y luego le enviamos un valor o accion
username = driver.find_element_by_css_selector("input[id='txtUsername']")
username.send_keys("Admin")
password = driver.find_element_by_css_selector("input[id='txtPassword']")
password.send_keys("admin123")
login_btn = driver.find_element_by_css_selector("input[id='btnLogin']")
time.sleep(1)
login_btn.click()

time.sleep(1)
# Cerramos la instancia(driver) actual
driver.close()