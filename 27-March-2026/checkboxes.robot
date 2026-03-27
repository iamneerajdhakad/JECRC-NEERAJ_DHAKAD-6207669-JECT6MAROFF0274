*** Settings ***
Documentation  handling checkbooxes
Library  SeleniumLibrary

*** Variables ***
${url_1}  https://the-internet.herokuapp.com/
${url_2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkbox herouapp
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url_1}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Checkboxes"]
    
    Page Should Contain Checkbox    xpath=//input[@type="checkbox"]
    
    Select Checkbox    xpath=//input[@type="checkbox"]
    Select Checkbox    xpath=//input[@type="checkbox"][2]

    Sleep    2s

    Unselect Checkbox    //input[@type="checkbox"][2]
    Sleep    2s

    Close Browser

Handling Checkbox Testautomation
    [Documentation]  Automation Testing Practice
    Open Browser  ${url_2}  chrome
    Maximize Browser Window
    Sleep    1s

    Input Text    xpath=//input[@id="name"]    "ABC"
    
    Select Checkbox  xpath=//input[@id="sunday"]
    Select Checkbox  xpath=//input[@id="monday"]
    Select Checkbox  xpath=//input[@id="tuesday"]
    Select Checkbox  xpath=//input[@id="wednesday"]
    Select Checkbox  xpath=//input[@id="thursday"]
    Select Checkbox  xpath=//input[@id="friday"]
    Select Checkbox  xpath=//input[@id="saturday"]
    
    Click Element    xpath=//input[@id="male"]
    Click Element    xpath=//input[@id="female"]

    Sleep    2s
