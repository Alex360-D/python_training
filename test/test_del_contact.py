# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test_contact"))
    app.contact.delete_first_contact()