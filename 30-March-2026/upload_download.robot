*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
*** Test Cases ***
File Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//a[text()="File Upload"]
    Click Element    xpath=//a[text()="File Upload"]

    Wait Until Element Is Visible    id=file-upload
    ${path}  Normalize Path    ${CURDIR}/Test.txt
    Choose File    id=file-upload    ${path}
    Wait Until Element Is Enabled    id=file-submit
    Click Element    id=file-submit
    Close Browser

File Download
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Wait Until Element Is Visible    xpath=//a[text()="File Download"]
    Click Element    xpath=//a[text()="File Download"]

    Wait Until Element Is Visible    id=content
    Click Element    xpath=//div[@id="content"]/descendant::a
    ${file_name}  Get Text    xpath=//div[@id="content"]/descendant::a
    Wait Until Created    C:\\Users\\neera\\Downloads\\${file_name}  timeout=10s
    File Should Exist    C:\\Users\\neera\\Downloads\\${file_name}
    Log To Console    Downloaded
    Close Browser
