# Import webdriver
from selenium import webdriver

import time

# Instaciar webdriver para chrome
driver = webdriver.Chrome("drivers/chromedriver")
# Maximizar ventana
driver.maximize_window()
# Acceso a la url
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# Acceder a un frame
driver.switch_to.frame("packageListFrame")
time.sleep(1)
# Acceder a un elemento del primer frame
link_frame_1 = driver.find_element_by_link_text("org.openqa.selenium")
link_frame_1.click()

# Cambiar el foco al marco predeterminado
driver.switch_to.default_content()

# Accedemos al segundo frame
driver.switch_to.frame("packageFrame")
# Acceder a un elemento del segundo frame
link_frame_2 = driver.find_element_by_link_text("By.Remotable")
link_frame_2.click()
time.sleep(1)

# Cambiar el foco al marco predeterminado
driver.switch_to.default_content()

# Accedemos al tercer frame
driver.switch_to.frame("classFrame")
# Acceder a un elemento del tercer frame
link_frame_3 = driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[8]")
link_frame_3.click()
time.sleep(1)

# Cambiar el foco al marco predeterminado
driver.switch_to.default_content()

time.sleep(3)
# Terminar la instacia de webdriver
driver.quit()

# New comment