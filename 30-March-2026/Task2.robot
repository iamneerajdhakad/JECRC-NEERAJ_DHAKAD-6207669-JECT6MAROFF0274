*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=alertBtn
    Click Element    id=alertBtn
    Handle Alert
    Close Browser

Handling Confirmation Alert (Accept)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=confirmBtn
    Click Element    id=confirmBtn
    Handle Alert
    Page Should Contain    You pressed OK!
    Close Browser

Handling Confirmation Alert (Dismiss)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=confirmBtn
    Click Element    id=confirmBtn
    Handle Alert    action=DISMISS
    Page Should Contain    You pressed Cancel!
    Close Browser

Handling Prompt Alert (Accept)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=promptBtn
    Click Element    id=promptBtn
    Input Text Into Alert    Hello World
    Page Should Contain    Hello World
    Close Browser

Handling Prompt Alert (dismiss)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=promptBtn
    Click Element    id=promptBtn
    Handle Alert  action=DISMISS
    Page Should Contain    User cancelled the prompt.
    Close Browser