# Importamos webdriver desde selenium
from selenium import webdriver
import time

# Instanciamos una variable con el driver del navegador a utilizar
driver = webdriver.Chrome(executable_path=("drivers/chromedriver"))
# Accedemos a la url de la app asignando la ruta con el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

# Localizamos los elementos utilizando la info del css
username = driver.find_element_by_css_selector("input#txtUsername")
username.send_keys("Admin")
password = driver.find_element_by_css_selector("input#txtPassword")
password.send_keys("admin123")
time.sleep(1)
login_btn = driver.find_element_by_css_selector("input#btnLogin")
login_btn.click()

time.sleep(1)
# Cerramos la instancia(driver) actual
driver.close()