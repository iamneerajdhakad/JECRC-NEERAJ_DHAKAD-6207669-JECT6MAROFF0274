*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Login Success  password=123  email=abc@gmail.com
    Sleep    3s

*** Keywords ***
Login Success
    [Arguments]  ${email}  ${password}=123
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${password}
