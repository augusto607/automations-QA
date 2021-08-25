*** Settings ***
# Referenciamos o importamos el archivo de recursos 
Resource    recursos1.robot

*** Test Case ***
# First automation
G001 Busqueda de palabras en google
    # Llamamos a nuestra keyword personalizada
    Open Browser and validate
    # Escribir un texto en el campo de busqueda (El texto sera: Casos de prueba)
    Input Text   xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input   ${palabrabuscar}
    # Click en un elemento cualquiera de la pagina para quitar la barra automatica de sugerencia
    Click Element   xpath=/html/body/div[1]/div[2]/div/img
    # Click en el boton buscar con google
    Click Element    xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]
    # Verificar el resultado de la busqueda utilizando el titulo de la pagina
    Title Should Be      ${palabrabuscar} - Google Search
    # Verificamos si el contenido deseado se encuentra en la pagina
    Page Should Contain      ${palabrabuscar}
    # Cerramos el navegador
    Close Browser