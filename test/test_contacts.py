# -*- coding: utf-8 -*-

import re
from model.contact import Contact

def test_contacts_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test_contact"))
    list_contacts_from_home_page = app.contact.get_contact_list()
    list_contacts_db = db.get_contact_list()
    assert sorted(list_contacts_from_home_page, key=Contact.id_or_max) == sorted(list_contacts_db, key=Contact.id_or_max)


    # assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    # assert contact_from_home_page.address == contact_from_edit_page.address
    # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))