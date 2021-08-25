# Importamos webdriver desde selenium
from selenium import webdriver

import time

# Instanciamos webdriver para chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")

# Accedemos a la url utilizando el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Identificamos en el DOM el valor del id del campo nombre usuario y lo
# referenciamos a una variable utilizando la funcion find_element_by_id
username = driver.find_element_by_id("txtUsername")

# Identificamos en el DOM el valor del id del campo clave de acceso y lo
# referenciamos a una variable utilizando la funcion find_element_by_id
password = driver.find_element_by_id("txtPassword")

# Incertar values en c/u de los campos identificados con la funcion send_keys
username.send_keys("Admin")
password.send_keys("admin123")

time.sleep(1)
# Identificamos en el DOM el valor del id del boton login y lo
# referenciamos a una variable utilizando la funcion find_element_by_id
login_btn = driver.find_element_by_id("btnLogin")

# Configuramos la accion del click sobre el boton con la funcion click
login_btn.click()

# Cerramos la sesion o instancia actual
driver.close()