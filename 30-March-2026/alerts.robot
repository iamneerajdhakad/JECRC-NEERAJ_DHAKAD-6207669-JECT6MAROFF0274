*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
handling simple alerts
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="JavaScript Alerts"]
    Sleep    1s
    Click Element    xpath=//button[@onclick="jsAlert()"]
    Handle Alert
    Sleep    3s
    Close Browser

Handling Confirmation Alert (accept)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="JavaScript Alerts"]
    Sleep    1s
    Click Element    xpath=//button[@onclick="jsConfirm()"]
    Handle Alert
    Sleep    3s
    Close Browser

Handling Confirmation Alert (Dismiss)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="JavaScript Alerts"]
    Sleep    1s
    Click Element    xpath=//button[@onclick="jsConfirm()"]
    Handle Alert  action=DISMISS
    Sleep    3s
    Close Browser

Handling Prompt Alert (Accept)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="JavaScript Alerts"]
    Sleep    1s
    Click Element    xpath=//button[@onclick="jsPrompt()"]
    Input Text Into Alert    Hello
    Sleep    3s
    Close Browser

Handling Prompt Alert (Dismiss)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="JavaScript Alerts"]
    Sleep    1s
    Click Element    xpath=//button[@onclick="jsPrompt()"]
    Sleep    1s
    Handle Alert  action=DISMISS
    Sleep    3s
    Close Browser
