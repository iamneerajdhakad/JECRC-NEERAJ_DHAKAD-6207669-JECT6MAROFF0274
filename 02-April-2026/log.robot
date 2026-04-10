*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Logging Demo
    Log To Console    Hello
    Log    Info Message
    Log    Debug Message  DEBUG
    Log    Warn Message  WARN
    Log    Error Message  ERROR
