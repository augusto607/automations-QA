# Import selenium webdriver
from selenium import webdriver

import time

# Instanciar webdriver para chrome
driver = webdriver.Chrome(executable_path="drivers/chromedriver")
# Obtener la url
driver.get("https://opensource-demo.orangehrmlive.com/")
# Maximizar ventana
driver.maximize_window()

# CLick open new window
link_orange = driver.find_element_by_partial_link_text("OrangeHRM")
link_orange.click()

# Referenciar el handle de ventana donde estamos posicionados
print(driver.current_window_handle)

# Retornar todos los handles que tenemos abiertos
handles = driver.window_handles
# recorremos la lista de los handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    # Cerrar la primera ventana
    if driver.title == "OrangeHRM":
        driver.close()

time.sleep(5)
# Terminar la instancia de webdriver
driver.quit()