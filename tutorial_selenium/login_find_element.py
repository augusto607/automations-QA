# Importamos webdriver desde selenium
from selenium import webdriver
# Importamos la clase By directamente desde selenium
from selenium.webdriver.common.by import By
import time

# Instanciamos una varible con el driver del navegador a utilizar
driver = webdriver.Chrome(executable_path=('drivers/chromedriver'))
# Obtenemos la pagina de nuestra app con el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')
# Maximisamos la ventana del navegador
driver.maximize_window()

# Instanciamos una busqueda de elemento invocando la clase By por el atributo name
username = driver.find_element(By.NAME, "txtUsername")
username.send_keys("admin")

time.sleep(1)
# Instanciamos una busqueda de elemento invocando la clase By por el atributo xpath
password = driver.find_element(By.XPATH, "//input[@id='txtPassword']")
password.send_keys("admin123")

# Instanciamos una busqueda de elemento invocando la clase By por el atributo id
login_btn = driver.find_element(By.ID, "btnLogin")
login_btn.click()

time.sleep(1)
# Instanciamos una busqueda de elemento invocando la clase By por el atributo link_text
link_1 = driver.find_element(By.LINK_TEXT, "Welcome Paul")
link_1.click()
# Instanciamos una busqueda de elemento invocando la clase By por el atributo partial_link_text
link_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
link_2.click()

time.sleep(1)
# Cerramos la instancia(driver) actual
driver.close()