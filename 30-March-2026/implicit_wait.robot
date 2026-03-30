*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
implicit wait 2
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Close Browser

implicit wait
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Set Selenium Implicit Wait    5s
    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser

implicit wait 3
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}

    Close Browser