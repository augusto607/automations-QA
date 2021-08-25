# Import selenium webdriver
from selenium import webdriver

import time

# Instanciar webdriver para firefox
driver = webdriver.Firefox(executable_path="drivers/geckodriver")
# Obtener la url
driver.get("http://testautomationpractice.blogspot.com/")
# Maximizar ventana del navegador
driver.maximize_window()
time.sleep(1)

# Buscar y click del boton alert
alert_btn = driver.find_element_by_xpath("//button[@onclick='myFunction()']")
alert_btn.click()
time.sleep(1)

# Hacer foco en la ventana de alerta o popup
#driver.switch_to_alert().accept() # Aceptar en la alerta
driver.switch_to_alert().dismiss() # Cancelar en la alerta

time.sleep(3)
# Terminar la instancia
driver.quit()