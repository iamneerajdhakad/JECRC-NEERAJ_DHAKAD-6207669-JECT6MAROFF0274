*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling window popup
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Scroll Element Into View    id=PopUp
    Click Element    id=PopUp
    Sleep    1s
    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}
    Switch Window  New
    Sleep    1s
    Switch Window  ${windows}[0]
    Sleep    5s
    Page Should Contain Element   xpath=//h1[contains(text(),"Automation")]

    Close Browser
    
