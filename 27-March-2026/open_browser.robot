*** Settings ***
Documentation  Opening of Browser
Library  SeleniumLibrary

*** Variables ***
#scalar variable stores one value
${url}  https://www.cricbuzz.com/

#list variable stores multi value
@{bikes}  ktm  kwasaki  honda  pulsar

# dict variable
&{cars}  nissan=gtr  honda=civic  bmw=m5

*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log    navigated to cricbuzz using chrome
    Log To Console    ${bikes}
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Log To Console    ${cars}
    Sleep    3s

    Close Browser

Open cricbuzz in edge
    Open Edge Browser

Opening Chrome Headless Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/ in headless mode
    ## tages are used to group test cases to run all the grouped test cases run (robot -d report -i "TAG_NAME" file_name.robot) -i is for include -e is for exclude
    [Tags]  smoke
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Log    navigated to cricbuzz using chrome
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close Browser


Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  headlessfirefox
    Maximize Browser Window

    Log    navigated to cricbuzz using fire fox
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close Browser

*** Keywords ***

Open Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log    navigated to cricbuzz using edge
    Log To Console    navigated to cricbuzz
    Sleep    3s

    Close Browser
