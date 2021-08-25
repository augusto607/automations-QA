# Importamos webdriver desde selenium
from selenium import webdriver
# Importamos la funcion de selenium para usar la clase select
from selenium.webdriver.support.ui import Select
import time

# Instanciamos un variable con el valor del ejecutable del navegador
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# Set URL
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximizamos una ventana del navegador
driver.maximize_window()

# Agregamos el codigo para iniciar la sesion en la app
username = driver.find_element_by_id("txtUsername")
username.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()

time.sleep(1)
# Enter en Admin
admin_menu = driver.find_element_by_id("menu_admin_viewAdminModule")
admin_menu.click()

time.sleep(1)
# Filter System User (invocamos a la funcion select para automatizar dropdown)
user_role_dropDown = Select(driver.find_element_by_id("searchSystemUser_userType"))
# Funcion select para seleccionar un valor del listado  por el indice
user_role_dropDown.select_by_index(2)

time.sleep(1)
# Filter Status
status_dropDown = Select(driver.find_element_by_id("searchSystemUser_status"))
# Fucion select para seleccionar un valor del listado por el value
status_dropDown.select_by_value("1")

time.sleep(1)
# Click boton search
search_btn = driver.find_element_by_id("searchBtn")
search_btn.click()

time.sleep(2)
# Cerramos la instancia(driver) actual
driver.close()