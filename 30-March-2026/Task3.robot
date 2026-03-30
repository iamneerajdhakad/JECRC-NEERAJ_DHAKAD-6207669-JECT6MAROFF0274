*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon Task
    Open Browser  ${url}  chrome
    Maximize Browser Window
    
    Wait Until Location Contains    amazon
    Wait Until Element Is Visible    xpath=//a[contains(text(),"Electronics")]
    Click Element    xpath=//a[contains(text(),"Electronics")]
    
    Scroll Element Into View    id=p_123-title
    Click Element    xpath=//input[@aria-labelledby="boAt"]/following::i
    Wait Until Element Is Visible    xpath=//div[@role="listitem"]
    ${product_name}  Get Text    xpath=//div[@role="listitem"]/descendant::div[@data-cy="title-recipe"]/descendant::h2/span
    
    Click Element    xpath=//div[@role="listitem"]/descendant::a
    Switch Window  New

    Sleep    3s
    Page Should Contain    ${product_name}
    ${product_price}  Get Text    xpath=//div[@class="a-section a-spacing-none aok-align-center aok-relative apex-core-price-identifier"]/descendant::span[@class="a-price-whole"]
    ${discount_percent}  Get Text    xpath=//div[@class="a-section a-spacing-none aok-align-center aok-relative apex-core-price-identifier"]/descendant::span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage apex-savings-percentage"]
    ${actual_price}  Get Text    xpath=//div[@class="a-section a-spacing-small aok-align-center"]/descendant::span[@class="a-price a-text-price apex-basisprice-value"]/span[2]

    Log To Console    Product price is: ${product_price}
    Log To Console    Discount percent is: ${discount_percent}
    Log To Console    Actual price is: ${actual_price}

    Scroll Element Into View    id=add-to-cart-button
    Click Element    id=add-to-cart-button
    Sleep    10s
    Click Element    xpath=//a[contains(@href,"nav_cart")]
    Sleep    2s
    
    Page Should Contain    ${product_name}
    Close Browser