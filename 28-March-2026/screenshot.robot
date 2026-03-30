*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
screenshot
    Set Screenshot Directory    ${CURDIR}/screenshot
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Capture Page Screenshot  fullpage.png
    Sleep    2s
    Scroll Element Into View    xpath=//div[text()="Dhurandhar The Revenge"]

    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  element.png