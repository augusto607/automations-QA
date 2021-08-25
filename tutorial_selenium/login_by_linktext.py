# Importamos webdriver desde selenium
from selenium  import webdriver
import time

# Instanciamos la busqueda del sitio con el navegador chrome
driver = webdriver.Chrome(executable_path=("drivers/chromedriver"))

# Accedemos a la url de nuestra app utilizando el metodo get
driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
# Declaramos una variable y asignamos la funcion find_element_by_link_text()
link_reset_password = driver.find_element_by_link_text("Forgot your password?")
# Configuramos el click con la funcion click()
link_reset_password.click()

time.sleep(1)
# Cerramos la instancia(driver) actual
driver.close()