*** Settings ***
Library     SeleniumLibrary

*** Variable ***
${homepage}     http://automationpractice.com/index.php
${browser}      chrome
${seleccion}    Other

*** Keywords ***
Select Women Option
    Click Element       xpath=//*[@id="block_top_menu"]/ul/li[1]/a
    Title Should Be     Women - My Store

Select Dresses Option
    Click Element       xpath=//*[@id="block_top_menu"]/ul/li[2]/a
    Title Should Be     Dresses - My Store

*** Test Case ***
002 Caso de prueba para validar con condicional if
    Open Browser    ${homepage}     ${browser}
    Wait Until Element Is Visible      xpath=//*[@id="header_logo"]/a/img
    # Declaramos la condicional
    Run Keyword If      '${seleccion}'=='Women'     Select Women Option     ELSE    Select Dresses Option
    Sleep       3s
    Close Browser