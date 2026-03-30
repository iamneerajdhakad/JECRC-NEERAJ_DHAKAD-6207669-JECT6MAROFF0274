*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Select Frame    id=singleframe
    
    Input Text    xpath=//input[@type="text"]    Hello Wold
    Sleep    2s

    Close Browser

Handling multi iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Click Element    xpath=//a[text()="Iframe with in an Iframe"]
    Sleep    1s
    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
    Sleep    1s
    Select Frame    xpath=//iframe[@src="SingleFrame.html"]
    Sleep    1s
    Input Text    xpath=//input[@type="text"]    Hello World
    Unselect Frame
    Page Should Contain     Automation Demo Site
    Sleep    2s
    Close Browser
