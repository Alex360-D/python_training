# -*- coding: utf-8 -*-

from pytest_bdd import given, when, then
from model.contact import Contact
import random
import pytest

# Add contact
@pytest.allure.step('Given a contact list')
@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@pytest.allure.step('Given a contact with lastname={lastname}, firstname={firstname}, address={address},'
                    ' home={home}, mobile={mobile}, work={work}, phone2={phone2}, email={email}, email2={email2} and email3={email3}')
@given('a contact with <lastname>, <firstname>, <address>, <home>, <mobile>, <work>, <phone2>, <email>, <email2> and <email3>')
def new_contact(lastname, firstname, address, home, mobile, work, phone2, email, email2, email3):
    return Contact(lastname=lastname, firstname=firstname, address=address,
                   home=home, mobile=mobile, work=work, phone2=phone2,
                   email=email, email2=email2, email3=email3)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    with pytest.allure.step('When I add the contact to the list'):
        app.contact.add(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        old_contacts = contact_list
        new_contacts = db.get_contact_list()
        old_contacts.append(new_contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# Delete contact
@pytest.allure.step('Given a non-empty contact list')
@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test_contact"))
    return db.get_contact_list()

@pytest.allure.step('Given a random contact from the list')
@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    with pytest.allure.step('When I delete the contact %s from the list' % random_contact):
        app.contact.delete_contact_by_id(random_contact.id)
    app.wd.implicitly_wait(5)

@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    with pytest.allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        old_contacts = non_empty_contact_list
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(random_contact)
        assert old_contacts == new_contacts
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# Modify contact
# @given('a non-empty contact list')
# def non_empty_contact_list(db, app):
#     if len(db.get_contact_list()) == 0:
#         app.contact.add(Contact(firstname="test_contact"))
#     return db.get_contact_list()

@pytest.allure.step('Given a random contact from the list')
@given('a random contact from the list')
def index_randrange_contact(non_empty_contact_list):
    return random.randrange(len(non_empty_contact_list))

@pytest.allure.step('Given a contact with lastname={lastname}, firstname={firstname}, address={address},'
                    ' home={home}, mobile={mobile}, work={work}, phone2={phone2}, email={email}, email2={email2} and email3={email3}')
@given('a contact with <lastname>, <firstname>, <address>, <home>, <mobile>, <work>, <phone2>, <email>, <email2> and <email3>')
def mod_contact(lastname, firstname, address, home, mobile, work, phone2, email, email2, email3):
    return Contact(lastname=lastname, firstname=firstname, address=address,
                   home=home, mobile=mobile, work=work, phone2=phone2,
                   email=email, email2=email2, email3=email3)

@when('I modify the contact in the list')
def modify_contact(app, non_empty_contact_list, index_randrange_contact, mod_contact):
    with pytest.allure.step('When I modify the contact %s in the listt' % mod_contact):
        old_contacts = non_empty_contact_list
        index = index_randrange_contact
        mod_contact.id = old_contacts[index].id
        app.contact.modify_contact_by_id(mod_contact.id, mod_contact)

@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, index_randrange_contact, mod_contact, check_ui):
    with pytest.allure.step('Then the new contact list is equal to the old list with the modified contact'):
        old_contacts = non_empty_contact_list
        index = index_randrange_contact
        new_contacts = db.get_contact_list()
        old_contacts[index] = mod_contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)