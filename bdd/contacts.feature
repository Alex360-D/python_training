Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <lastname>, <firstname>, <address>, <home>, <mobile>, <work>, <phone2>, <email>, <email2> and <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | lastname  | firstname  | address  | home  | mobile  | work  | phone2  | email  | email2  | email3  |
  | lastname1 | firstname1 | address1 | home1 | mobile1 | work1 | phone1  | email1 | email1  | email1  |
  | lastname2 | firstname2 | address2 | home2 | mobile2 | work2 | phone2  | email2 | email2  | email2  |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <lastname>, <firstname>, <address>, <home>, <mobile>, <work>, <phone2>, <email>, <email2> and <email3>
  When I modify the contact in the list
  Then the new contact list is equal to the old list with the modified contact

  Examples:
  | lastname     | firstname     | address      | home      | mobile      | work      | phone2      | email      | email2      | email3      |
  | lastname_mod | firstname_mod | address_mod  | home_mod  | mobile_mod  | work_mod  | phone2_mod  | email_mod  | email2_mod  | email3_mod  |