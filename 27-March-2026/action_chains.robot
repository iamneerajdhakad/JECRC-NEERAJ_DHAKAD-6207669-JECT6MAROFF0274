*** Settings ***
Documentation  action chain
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
Handling Drag and Drop
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[text()="Drag and Drop"]
    Drag And Drop    id=column-a    id=column-b
    Sleep    2s

Handling mouse hover
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Click Element    xpath=//a[text()="Hovers"]
    Sleep    2s
    Mouse Over    xpath=//div[@class="figure"][2]
    Sleep    2s
    Close Browser

Handling Scroll To Element
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    
    Scroll Element Into View    xpath=//a[text()="Typos"]
   
    
    
    