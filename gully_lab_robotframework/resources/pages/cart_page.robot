*** Settings ***
Library  SeleniumLibrary
Resource  ../common_resorces.robot
Resource  ../../locators/cart_page_locators.robot

*** Keywords ***
Add To Cart
    Click Element    ${first_product}
    Sleep    2s
    Click Element    ${gender}
    Sleep    2s
    Select From List By Value    ${size}  UK 7
    Sleep    2s    Click Element    ${add_ot_cart_btn}
    Sleep    2s
    Page Should Contain    Cart