*** Settings ***
Documentation  Drop down handling
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url_2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Drop Down
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[text()="Dropdown"]

    Page Should Contain List    id=dropdown

    ${options}  Get List Items    id=dropdown
    Log To Console    ${options}
    Select From List By Label    id=dropdown  Option 1
    Select From List By Index    id=dropdown  2

    ${select_option}  Get Selected List Label    id=dropdown
    Log To Console    ${select_option}

    List Selection Should Be    id=dropdown  Option 2
    Sleep    3s

    Close Browser
    
Handling MultiSelect Dropdown
    Open Browser  ${url_2}  chrome
    Maximize Browser Window
    
    Scroll Element Into View    locator
