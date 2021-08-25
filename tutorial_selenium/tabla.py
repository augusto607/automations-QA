# Importamos webdriver desde selenium
from selenium import webdriver

# Instanciamos una variable con el path del ejecutable del navegador
driver = webdriver.Chrome("drivers/chromedriver")

# Maximisamos la ventana del navegador
driver.maximize_window()

# Optenemos la ruta de nuestra app con el comando get
driver.get("file:/Users/augusto607/Documents/Learning/QA/Python_Selenium_WebDriver/resourses/table.html")

# Instanciamos una variable con una busqueda por xpath para conocer el # filas
rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
# Instanciamos una variable con una busqueda por xpath para conocer el # columnas
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td"))

# Imprimimos las filas y luego las columnas
print(rows)
print(cols)

# Imprimimos los titulos de la tabla
print("Company"+"           "+"Contact"+"           "+"Country")
# Recorremos los valores de las filas y columnas
for r in range(2, rows+1):
    for c in range(1, cols+1):
        # Con find_by_xpath iteramos todos los elementos de las columnas tomandolos con el metodo .text
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='             ')
    print()

# Cerramos la instancia(driver) actual
driver.close()