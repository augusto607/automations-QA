*** Settings ***
Library     SeleniumLibrary
Library     String

*** Variable ***
${browser}      chrome
${homepage}     http://automationpractice.com/index.php

*** Keywords ***
Open homepage
    Open Browser        ${homepage}     ${browser}

*** Test Case ***
C001 Click en contenedores
    Open homepage
    # Definir una variable global que sea un array(se declara con el @)
    Set Global Variable     @{nombreContenedores}       //*[@id="homefeatured"]/li[1]/div/div[2]/h5/a   
    ...     //*[@id="homefeatured"]/li[2]/div/div[2]/h5/a   //*[@id="homefeatured"]/li[3]/div/div[2]/h5/a

    # Ciclo loop for
    FOR    ${container}    IN      @{nombreContenedores}
        Click Element   xpath=${container}
        Wait Until Element Is Visible   xpath=//*[@id="center_column"]/div/div/div[2]
        Click Element   xpath=//*[@id="header_logo"]/a/img
    END

    Sleep                   1s
    Close Browser
