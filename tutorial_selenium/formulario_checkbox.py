# Importamos webdriver desde selenium
from selenium import webdriver
# Importamos la funcion de selenium para usar la clase select
from selenium.webdriver.support.ui import Select
import time

# Instanciamos un variable con el valor del ejecutable del navegador
driver = webdriver.Chrome(executable_path='drivers/chromedriver')

# Put URL
driver.get("https://opensource-demo.orangehrmlive.com/")

# Maximizamos una ventana del navegador
driver.maximize_window()

# Enter login code
username = driver.find_element_by_id("txtUsername")
username.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()

time.sleep(1)

# Enter menu PIM
pim_menu = driver.find_element_by_id("menu_pim_viewPimModule")
pim_menu.click()

time.sleep(1)
# Enter en menu Configuracion
menu_conf = driver.find_element_by_id("menu_pim_Configuration")
menu_conf.click()

time.sleep(1)
# Enter in optional fields
optional_fields = driver.find_element_by_id("menu_pim_configurePim")
optional_fields.click()

# Select checkbox
list_checkbox = driver.find_elements_by_css_selector("li[class='checkbox']>input")

# Boton Edit/Save
edit_btn = driver.find_element_by_id("btnSave")

# Recorremos todos los checkbox de la lista
for checkbox in list_checkbox:
    if checkbox.is_displayed() is True and checkbox.is_enabled() is False:
        edit_btn.click()
        time.sleep(1)
    if checkbox.is_displayed() is True and checkbox.is_selected() is False:
        time.sleep(1)
        checkbox.click()
    else:
        checkbox.click()

edit_btn.click()

time.sleep(2)
# Kill drive
driver.quit()