*** Settings ***
Resource  ../../resources/common_resorces.robot
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/pages/cart_page.robot
Resource    ../../resources/pages/search_page.robot
Resource    ../../locators/cart_page_locators.robot


Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC_05 verify product in cart
    Clicking On Accounts
    Login To GullyLabs    ${USER_EMAIL}    ${USER_PWD}
    Search a product  Shoes
    Add To Cart
    ${product}  Get Text    ${product_name}
    Log To Console    ${product}
    Sleep    2s
    ${in_cart}  Get Text    ${product_name_in_cart}
    Should Contain    ${in_cart}    ${product}

