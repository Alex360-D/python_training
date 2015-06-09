# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_modify_some_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Alexander_modif")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test_contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Alexander_mod", middlename="Alex_mod", lastname="Paderin_mod", nickname="Alex360_mod",
                      title="Alex-title_mod", company="Alex Company_mod", address="Russia, Moscow City, 11_mod",
                      home="+7(495)111-11-11_mod", mobile="+7(495)222-22-22_mod", work="+7(495)333-33-33_mod",
                      fax="+7(495)444-44-44_mod", email="alex@alex.ru_mod", email2="alex2@alex.ru_mod",
                      email3="alex3@alex.ru_mod", homepage="http://alexhomepage.ru_mod", byear="1985",
                      address2="Russia, Moscow City, 15_mod", phone2="5555_mod", notes="simple notes_mod")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)