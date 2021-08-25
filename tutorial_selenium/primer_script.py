# Importamos las dependencias de webdriver desde seleniun
from selenium import webdriver

import time

# Declaramos una variable para instanciar webdriver para chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")

# Llamamos al metodo para maximizar una ventana del navegador
driver.maximize_window()

# Llamamos a la funcion get para pasarle la url de la pagina a automatizar
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(5)

# Llamamos el metodo quit para matar la instacia
driver.quit()