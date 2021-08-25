# Importamos webdriver desde selenium
from selenium import webdriver
import time

# Instanciamos webdriver para chrome
driver = webdriver.Chrome(executable_path=("drivers/chromedriver"))

# Accedemos a la url utilizando el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Instaciamos a una variable con la funcion find_element_by_name buscando el valor del campo del usuario
username = driver.find_element_by_name("txtUsername")
# Ingresamos el valor del nombre de usuario
username.send_keys("Admin")
# Instaciamos a una variable con la funcion find_element_by_name buscando el valor del campo clave
password = driver.find_element_by_name("txtPassword")
time.sleep(1)
# Ingresamos el valor del password
password.send_keys("admin123")
# Instaciamos a una variable con la funcion find_element_by_name buscando el valor del boton login
login_btn = driver.find_element_by_name("Submit")
# Simulamos el click del boton login con la funcion click()
login_btn.click()

time.sleep(3)
# Cerramos la instancia(driver) actual
driver.close()