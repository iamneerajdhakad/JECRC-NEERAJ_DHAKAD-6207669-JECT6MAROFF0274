*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Click Element    xpath=//a[text()="Multiple Windows"]
    Sleep    2s
    Click Element    xpath=//a[@href="/windows/new"]
    Sleep    2s
    
    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    
    Page Should Contain    New Window
    Page Should Contain Element    xpath=//h3[text()="New Window"]

    Switch Window  ${windows}[0]
    Sleep    2s
    Close Browser
    

    