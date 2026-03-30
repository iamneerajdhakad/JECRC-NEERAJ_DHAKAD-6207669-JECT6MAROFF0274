*** Settings ***
Documentation  Drop down handling
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling MultiSelect Dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Scroll Element Into View    id=colors

    ${options}  Get List Items    id=colors

    Select From List By Label    id=colors  Blue
    Select From List By Index    id=colors  2
    Select From List By Value    id=colors  yellow


    ${selected_options}  Get Selected List Values    id=colors
    Log To Console    ${selected_options}
    List Selection Should Be    id=colors  Blue  Yellow  Green

    Sleep    5s
    Close Browser