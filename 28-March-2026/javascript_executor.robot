*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handling js
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Sleep    1s

    Execute Javascript  window.scrollTo(0,document.body.scrollHeight)
    Sleep    2s
    Execute Javascript  window.scrollTo(0,0)
    Sleep    2s
    Execute Javascript  window.scrollTo({top: 10000, behavior: 'smooth'})
    Sleep    10s

