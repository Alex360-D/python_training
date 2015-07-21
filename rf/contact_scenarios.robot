*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  lastname-1  firstname-1  address-1  home-1  mobile-1  work-1  phone2-1  email-1  email2-1  email3-1
    Add Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  lastname_test  firstname_test  address_test  home_test  mobile_test  work_test  phone2_test  email_test  email2_test  email3_test
    Run Keyword If  ${len}== 0  Add Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  lastname_test  firstname_test  address_test  home_test  mobile_test  work_test  phone2_test  email_test  email2_test  email3_test
    Run Keyword If  ${len}== 0  Add Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${source_contact}=  Get From List  ${old_list}  ${index}
    ${new_data_contact}=  New Contact  lastname_mod  firstname_mod  address_mod  home_mod  mobile_mod  work_mod  phone2_mod  email_mod  email2_mod  email3_mod
    Modify Contact  ${source_contact}  ${new_data_contact}
    ${new_list}=  Get Contact List
    Set List Value  ${old_list}  ${index}  ${new_data_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}