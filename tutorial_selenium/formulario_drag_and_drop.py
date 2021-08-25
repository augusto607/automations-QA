# Import webdriver from selenium
from selenium import webdriver
# Importamos ActionChain para automatizar drag and drops
from selenium.webdriver.common.action_chains import ActionChains

import time

# Creamos una instancia webdriver para chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")

# Maximizamos la ventana del navegador
driver.maximize_window()

# Set URL
driver.get("http://www.dhtmlgoodies.com/scripts/arrange-table-rows/demo.html")

time.sleep(1)
# Instanciamos el ActionChains
action = ActionChains(driver)
# Elemento Origen
source = driver.find_element_by_xpath("//tr[@id='row1']")
# Elemento Destino
target = driver.find_element_by_xpath("//tr[@id='row9']")


# Ejecutamos el drag and drop
action.drag_and_drop(source=source, target=target).perform()


time.sleep(2)
# Kill driver
driver.quit()
