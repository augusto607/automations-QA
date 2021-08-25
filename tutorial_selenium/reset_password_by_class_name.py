# Importamos webdriver desde selenium
from selenium import webdriver
import time

# Instanciamos nuestra prueba con los drivers del navegador a usar
driver = webdriver.Chrome(executable_path=("drivers/chromedriver"))

# Accedemos a la url de nuestra app con el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Declaramos una variable y asignamos la funcion find_element_by_link_text()
link_reset_password = driver.find_element_by_link_text("Forgot your password?")
# Configuramos el click con la funcion click()
link_reset_password.click()
time.sleep(1)
# Como el campo a localizar no contine el atributo class lo automatizaramos por el id
reset_username = driver.find_element_by_id("securityAuthentication_userName")
# Asignamos el valor de este campo
reset_username.send_keys("Admin")
time.sleep(1)
# Localizamos el boton de reset clave utilizando el metodo find_element_by_class_name
reset_password_btn = driver.find_element_by_class_name("searchValues")
# Utilizamos la funcion click() para presionar
reset_password_btn.click()

time.sleep(2)
# Cerramos la instancia(driver) actual
driver.close()