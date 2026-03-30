*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Explicit wiat
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Wait Until Element Is Visible    id=username
    Input Text    id=username    student

    Wait Until Element Is Visible    id=password
    Input Text    id=password    Password123

    Wait Until Element Is Enabled    id=submit
    Click Element    id=submit

    Wait Until Location Contains    logged-in-successfully

    Close Browser


