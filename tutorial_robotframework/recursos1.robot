*** Settings ***
Documentation   Existe un documento de texto con toda la informacion 
...             Primera automatizacion con robot framework
Library     SeleniumLibrary

*** Variable ***
${palabrabuscar}    Casos de prueba
${URL}              http://google.com
${Navegador}        chrome

*** Keywords ***
Open Browser and validate
    # Abrir el navegador google chrome
    Open Browser     ${URL}     ${Navegador}
    # Click en aceptar las politicas de google 
    Click Element   xpath=//*[@id="L2AGLb"]
    # Esperar a que se carge un elemento de la pagina y lo localizaremos por xpath
    Wait Until Element Is Visible 	 xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]