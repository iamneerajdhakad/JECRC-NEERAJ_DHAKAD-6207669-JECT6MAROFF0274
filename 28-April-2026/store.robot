*** Settings ***
Library  RequestsLibrary
Library  Collections

#Test Setup  Create Session    petapi    ${BASE_URL}  verify=True

*** Variables ***
${BASE_URL}  https://petstore.swagger.io/v2

*** Test Cases ***
Pet inventories
    [Documentation]  Get pet inventories by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session  petapi  /store/inventory
    Should Be Equal As Integers  ${response.status_code}  200

    ${body}=  Set Variable  ${response.json()}
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Place Order
    [Documentation]  Place an order for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Create Dictionary
    ...  id=12345
    ...  petId=54321
    ...  quantity=1
    ...  shipDate=2024-06-01T12:00:00.000
    ...  status=placed
    ...  complete=false

    ${response}=  POST On Session  petapi  /store/order  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=  Set Variable  ${response.json()}
    Should Be Equal As Integers    ${body}[id]    12345
    Set Suite Variable    ${ORDER_ID}    ${body}[id]

Get using ID
    [Documentation]  Get order by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session  petapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=  Set Variable  ${response.json()}
    Should Be Equal As Integers    ${body}[id]    ${ORDER_ID}

Delete using ID
    [Documentation]  Delete order by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  DELETE On Session  petapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response.status_code}    200

E2E
    Create Session    e2eapi    ${BASE_URL}  verify=True

    ${payload}=  Create Dictionary
    ...  id=29
    ...  petId=51
    ...  quantity=1
    ...  shipDate=2024-06-01T12:00:00.000
    ...  status=placed
    ...  complete=false

    ${res1}=  POST On Session  e2eapi  /store/order  json=${payload}
    Should Be Equal As Integers    ${res1.status_code}    200
    Log To Console    Created an order
    ${body}=  Set Variable  ${res1.json()}
    Set Suite Variable    ${ORDER_ID}   ${body}[id]

    ${res2}=  GET On Session  e2eapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    Retrieved the order

    ${res3}=  DELETE On Session  e2eapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    Deleted the order