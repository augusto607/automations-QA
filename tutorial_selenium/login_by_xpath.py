# Importamos webdriver desde selenium
from selenium import webdriver
import time

# Instanciamos una variable con el driver ejecutable del navegador que vamos a utilizar
driver = webdriver.Chrome(executable_path=("drivers/chromedriver"))
# Indicamos cual es la ruta url de nuestra app con el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Empezamos a realizar la busqueda de los diferentes elementos
username = driver.find_element_by_xpath("//input[@name='txtUsername']")
username.send_keys("Admin")
password = driver.find_element_by_xpath("//input[@name='txtPassword']")
time.sleep(1)
password.send_keys("admin123")
login_btn = driver.find_element_by_xpath("//input[@name='Submit']")
login_btn.click()

time.sleep(1)
# Cerramos la instancia(driver) actual
driver.close()