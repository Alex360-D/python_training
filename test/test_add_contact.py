# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest

def test_add_contact(app, db, json_contacts, check_ui):
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    contact = json_contacts
    with pytest.allure.step('When I add the contact %s to the list' % contact):
        app.contact.add(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        with pytest.allure.step('Also check UI'):
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)