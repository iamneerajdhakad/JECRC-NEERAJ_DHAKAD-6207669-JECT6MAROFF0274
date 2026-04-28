*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  JSONLibrary

*** Variables ***
${BASE_URL}  https://petstore.swagger.io/v2

*** Test Cases ***
Add a pet
    [Documentation]  Upload an image for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet_to_store.json
    ${response}=  POST On Session  petapi  /pet  json=${payload}
    ${body}=  Set Variable  ${response.json()}
    Set Suite Variable    ${PET_ID}   ${body}[id]
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Upload a Image
    Create Session    petapi    ${BASE_URL}  verify=True

    ${formdata}=  Create Dictionary  additionalMetadata=Test
    ${file_path}=  Set Variable  ${CURDIR}/../data/img.jpeg
    ${file}=  Evaluate    {'file': open(r'${file_path}','rb')}
    ${response}=  POST On Session  petapi  /pet/${PET_ID}/uploadImage  data=${formdata}  files=${file}
    Should Be Equal As Integers    ${response.status_code}    200

Update a pet
    [Documentation]  Update an existing pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet_in_store.json
    ${response}=  PUT On Session  petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Find by Status
    [Documentation]  Find pets by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=  Create Dictionary  status=available
    ${response}=  GET On Session  petapi  /pet/findByStatus  params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Get a pet by ID
    [Documentation]  Get a pet by its ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  GET On Session  petapi  /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Update a pet using form data
    [Documentation]  Update a pet's name and status using form data
    Create Session    petapi    ${BASE_URL}  verify=True
    ${formdata}=  Create Dictionary  name=UpdatedPetName  status=sold
    ${response}=  POST On Session  petapi  /pet/${PET_ID}  data=${formdata}
    Should Be Equal As Integers    ${response.status_code}    200

Delete a pet
    [Documentation]  Delete a pet by its ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=  DELETE On Session  petapi  /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200